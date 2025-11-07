# 여기에 코드를 작성해주세요.

import streamlit as st
import pandas as pd
import numpy as np

# 샘플 데이터
data = {
    "요일": ["월", "화", "수", "목", "금"],
    "1교시": ["물리학", "생물학2", "물리학", "생물학2", "컴탐"],
    "2교시": ["", "", "", "", "생실"],
    "3교시": ["물실", "조선의 역사적 성취와 유산", "", "조선의 역사적 성취와 유산", ""],
    "4교시": ["", "대학글쓰기1", "", "대학글쓰기1", ""]
}
df = pd.DataFrame(data)

# st.table(): 정적인 테이블 표시
st.write("### 정적 시간표")
st.table(df)

# st.json(): JSON 구조 표시
json_data = {
    "물리학": {"교수": "문송기", "강의실": "26동 B101호"},
    "생물학2": {"교수": "신혜영, 주용성, 조형택", "강의실": "28동 302호"},
    "컴탐": {"교수": "변해선", "강의실": "26동 104호"}
}
st.write("### JSON 데이터")
st.json(json_data)

# 지표(숫자+증감률)
st.metric(label="수강 과목 수", value="6")
st.metric(label="총 학점", value="16", delta="+0")
