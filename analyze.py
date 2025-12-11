import pandas as pd

positive_words = [
    "성공", "호재", "상승", "개선", "강세", "혁신", "안정", "회복", "돌파",
    "축하", "진전", "강화", "확대", "호황", "수혜", "신기록", "급증",
    "호평", "긍정", "효과", "발견", "도약", "주요", "강력",
    "급성장", "최고", "선도", "기대", "희망", "진보", "승인", "완화",
    "개발", "발전", "달성", "가속", "성과", "순항", "성장",
    "약진", "선정", "성료", "증가"
]

negative_words = [
    "폭락", "하락", "추락", "악재", "감소", "약세", "논란", "위기", "중단",
    "연기", "취소", "비판", "우려", "경고", "피해", "사망", "사고",
    "악화", "축소", "퇴보", "불안", "불만", "적자", "실망", "문제",
    "부진", "중단", "차질", "경질", "붕괴", "파문", "갈등", "혼란",
    "급감", "실종", "패배", "침체", "구속", "징역", "부도", "파산",
    "폭발", "악성", "추가 피해", "불확실", "공포", "위험"
]

def analyze_news(df):
    sentiments = []
    for title in df["title"]:
        score = 0
        for w in positive_words:
            if w in title:
                score += 1
        for w in negative_words:
            if w in title:
                score -= 1

        if score > 0:
            sentiments.append("긍정")
        elif score < 0:
            sentiments.append("부정")
        else:
            sentiments.append("중립")

    df["sentiment"] = sentiments
    return df
