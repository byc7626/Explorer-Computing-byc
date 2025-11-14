import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("C:/Users/dal76/OneDrive/Desktop/컴퓨팅/컴퓨팅 탐색/cars.csv")
    return df

def cars_home():
    #자동차 연비 대시보드의 주요 목적과 활용 포인트를 소개한다.
    st.title("🚗 자동차 연비 분석 대시보드")

    st.write("""
    이 대시보드는 자동차 성능 데이터를 기반으로  
    **대륙별 평균 연비, 마력(hp)과 연비(mpg) 관계, 차량 무게와 연비 관계, 연도별 평균 연비 변화**등을 시각화합니다.
    """)

    st.markdown("---")

    st.subheader("📊 주요 기능")
    st.markdown("""
    1. **탐색적 자료분석 (EDA)**  
       - 제조 대륙별 평균 연비 비교, 마력과 차량 무게 대비 연비 분포, 연도별 연비 변화 등을 시각화합니다.  
       - 그래프를 통해 데이터를 직관적으로 확인할 수 있습니다.  

    2. **연비 예측**  
       - 차량의 제원(`hp`, `weightlbs`, `cubicinches`, `cylinders`)을 입력하면  
         머신러닝 모델이 예상 연비를 예측합니다.  

    3. **실시간 인터랙티브 시각화**  
       - 슬라이더, 드롭다운 등 Streamlit 위젯을 활용하여  
         조건을 바꾸면 그래프가 **즉시 업데이트**됩니다.
    """)

    st.markdown("---")

    st.subheader("💡 활용 포인트")
    st.info("""
    - 데이터를 시각화하며 **연비에 영향을 주는 변수**를 탐색할 수 있습니다.  
    - 사용자가 직접 조건을 조정하면서 **예상 연비 모델의 반응**을 실시간으로 확인할 수 있습니다.  
    - Streamlit을 활용해 **웹 기반 데이터 분석 대시보드** 제작을 체험할 수 있습니다.
    """)

    st.markdown("---")

    st.caption("📁 데이터 출처: Kaggle - Auto MPG Dataset")

def cars_EDA(df):
    #연비(mpg)와 주요 변수 간의 관계, 대륙별 특성, 연도별 변화 등을 시각적으로 분석한다.
    st.title("🔍 자동차 연비 분석 (EDA)")

    st.write("""
    이 탭에서는 자동차 성능 데이터를 활용하여  
    **연비(mpg)와 주요 변수들 간의 관계, 대륙별 특성, 연도별 변화** 등을 탐색합니다.
    """)

    # 데이터 미리보기
    st.subheader("📄 데이터 미리보기")
    st.dataframe(df.head())

    st.markdown("---")

def cars_predict():
    #머신러닝 모델을 활용하여 자동차의 연비를 예측하는 기능을 구현한다. 
    pass

def main():
    st.set_page_config(page_title="자동차 연비 대시보드", layout="wide")

    # --- 사이드바 메뉴 ---
    menu = st.sidebar.radio(
        "대시보드 메뉴",
        ["홈", "탐색적 자료분석(EDA)", "연비 예측"]
    )

    df = load_data()

    # --- 홈 화면 ---
    if menu == "홈":
        cars_home()

    # --- 탐색적 자료분석 화면 ---
    elif menu == "탐색적 자료분석(EDA)":
        cars_EDA(df)

    # --- 연비 예측 화면 ---
    elif menu == "연비 예측":
        cars_predict() 


if __name__ == "__main__":
    main()
