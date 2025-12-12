import streamlit as st
import pandas as pd
from scraper import get_news
from analyze import analyze_news

st.title("📰 뉴스 헤드라인 감성 분석")

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
