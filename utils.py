from datetime import datetime

import pandas as pd
import pytz

import requests
from bs4 import BeautifulSoup


def get_today():
    # 오늘 날짜를 YYYY-MM-DD 형식으로 반환
    today = datetime.now(pytz.utc)
    return today.strftime("%Y-%m-%d")


def update_paper_list(paper_title, paper_url, filename="paper_logs/papers_list.csv"):
    exists_paper = False

    df = pd.read_csv(filename)

    # 논문 제목이 DataFrame에 없는 경우 추가
    if paper_title not in df["title"].values:
        dates = df["date"].values.tolist()
        titles = df["title"].values.tolist()
        urls = df["url"].values.tolist()
        dates.append(get_today())
        titles.append(paper_title)
        urls.append(f"https://arxiv.org/abs/{paper_url.split('/papers/')[-1]}")
        df = pd.DataFrame(data={"date": dates, "title": titles, "url": urls})
        df.to_csv(filename, index=False, encoding="utf-8")
        exists_paper = False
        print(f"Added '{paper_title}' to {filename}")
    else:
        exists_paper = True
        print(f"'{paper_title}' already exists in {filename}")

    return not exists_paper

def get_html_experimental_link(paper_url):
    response = requests.get(paper_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 'HTML (experimental)' 링크 찾기
    html_link = soup.find("a", string="HTML (experimental)")
    if html_link:
        return html_link["href"]  # 링크 추출
    else:
        return "Link not found"