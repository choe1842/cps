import requests
from bs4 import BeautifulSoup

# 1.

res = requests.get("https://kr.indeed.com/jobs?q=%EB%8C%80%EA%B8%B0%EC%97%85&fromage=last&sort=date")

print(res)

if res.status_code != 200 :
    print("request error : ", res.status_code)


# 2.

html = res.text

soup = BeautifulSoup(html, "html.parser")

pages = soup.select(".pagination > a")

print(len(pages))
