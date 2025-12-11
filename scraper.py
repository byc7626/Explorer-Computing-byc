import requests
from bs4 import BeautifulSoup
import pandas as pd

CATEGORY_URL = {
    "정치": "https://news.naver.com/section/100",
    "경제": "https://news.naver.com/section/101",
    "사회": "https://news.naver.com/section/102",
    "생활/문화": "https://news.naver.com/section/103",
    "세계": "https://news.naver.com/section/104",
    "IT/과학": "https://news.naver.com/section/105"
}

def get_news(category):
    url = CATEGORY_URL.get(category)

    if url is None:
        raise ValueError("유효하지 않은 카테고리입니다.")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []
    dates = []

    articles = soup.select(".sa_item")
    for a in articles:
        title_tag = a.select_one(".sa_text_strong")
        date_tag = a.select_one(".sa_text_timestamp")

        if title_tag:
            titles.append(title_tag.get_text(strip=True))
        else:
            titles.append("제목 없음")

        if date_tag:
            dates.append(date_tag.get_text(strip=True))
        else:
            dates.append("날짜 없음")

    df = pd.DataFrame({
        "title": titles,
        "date": dates
    })
    return df
