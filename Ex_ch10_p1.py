# 아래에 코드를 작성해주세요.
import streamlit as st
import pandas as pd

st.title("이름")
st.header("배윤채")

st.subheader("정보")
st.write({"나이": "만 19세", 
"전공": "생명과학부", 
"학번": "25", 
"혈액형": "B형", 
"MBTI": "ENTJ", 
"종교": "개신교"})

st.subheader("취미")
st.write(pd.DataFrame({"**음악**": ["바이올린", "피아노", "노래", "플루트"]}, 
{"유튜브": ["요리", "게임", "ASMR", "코미디 스케치"]}))

st.markdown("# 자기소개 글")
st.write("안녕! **윤채**의 strealit에 온 걸 환영해! 내 소개 잘 봤지? *앞으로 서로 더 알아가자!*")
st.write("Hi! Welcome to **Yunchae’s** Streamlit! Did you enjoy my introduction? *Let’s get to know each other better from now on!*")
