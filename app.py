#app.py

import streamlit as st
import pandas as pd
from scraper import get_news
from analyze import analyze_news

st.title("📰 뉴스 헤드라인 감성 분석")

st.header("이런 데이터가 쓰였어요!")
st.write(
    "네이버 뉴스(https://news.naver.com/)의 정치, 경제, 사회, 생활/문화, IT/과학, 세계 키워드별 최신 뉴스의 헤드라인을 스크랩하여 데이터로 이용합니다."
)

st.header("이렇게 분석했어요!")
st.write(
    """긍정, 부정 단어 리스트를 정의하고,
    뉴스의 헤드라인에 포함된 단어 수를 비교하여 감성을 분석했어요.
    
    📌긍정 단어가 더 많이 포함되었다면? - 긍정
    📌부정 단어가 더 많이 포함되었다면? - 부정
    📌두 단어가 모두 없거나 개수가 동일하다면? - 중립"""
)

category = st.selectbox("뉴스 카테고리 선택", ["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"])

if st.button("뉴스 불러오기"):
    df = get_news(category)
    analyzed_df = analyze_news(df)

    st.write("### 전체 감성 분석 결과")
    st.dataframe(analyzed_df)

    # 긍정만
    st.markdown("## 🟢 긍정 뉴스 모아보기")
    positive_df = analyzed_df[analyzed_df["sentiment"] == "긍정"]

    if len(positive_df) > 0:
        for idx, row in positive_df.iterrows():
            st.markdown(
                f"""
                <div style="padding: 10px; margin: 8px 0; border-radius: 10px; background-color:#e3fcef;">
                    <b>{row['title']}</b><br>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write("긍정 뉴스가 없습니다.")

    # 부정만
    st.markdown("## 🔴 부정 뉴스 모아보기")
    negative_df = analyzed_df[analyzed_df["sentiment"] == "부정"]

    if len(negative_df) > 0:
        for idx, row in negative_df.iterrows():
            st.markdown(
                f"""
                <div style="padding: 10px; margin: 8px 0; border-radius: 10px; background-color:#fdecea;">
                    <b>{row['title']}</b><br>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write("부정 뉴스가 없습니다.")

    result=[]

    if len(positive_df) > len(negative_df):
        result="긍정 뉴스가 더 많아요!"
    elif len(positive_df) < len(negative_df):
        result="부정 뉴스가 더 많아요!"
    else:
        result="긍정 뉴스와 부정 뉴스의 개수가 같아요!"
    

    st.header("분석 결과")
    st.write(
        f"""{category} 키워드의 뉴스 헤드라인 감성 분석 결과, 긍정 뉴스가 {len(positive_df)}개, 부정 뉴스가 {len(negative_df)}개로 {result}"""
    )
