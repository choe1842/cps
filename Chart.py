import requests
from bs4 import BeautifulSoup
import csv

class Scraper():

    def __init__(self):
        self.url = "https://www.melon.com/chart/index.htm"

    def getHTML(self):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}  # request 500 현상이 발생해 헤더를 추가했습니다.
        res = requests.get(self.url, headers=header)
        if res.status_code != 200:
            print("bad request", res.status_code)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def getchart(self, soup):
        RANK = 100

        titles = soup.find_all("div", {"class": "ellipsis rank01"})
        singers = soup.find_all("div", {"class": "ellipsis rank02"})
        albums = soup.find_all("div", {"class": "ellipsis rank03"})

        Title = []
        Singer = []
        Album = []

        for t in titles:
            Title.append(t.find('a').text)

        for s in singers:
            Singer.append(s.find('span', {"class": "checkEllipsis"}).text)

        for a in albums:
            Album.append(a.find('a').text)

        self.writeCSV(Title, Singer, Album)

    def writeCSV(self, Title, Singer, Album) :
        file = open("chart.csv", "a", newline="")

        wr = csv.writer(file)

        for i in range(len(Title)):
            wr.writerow([str(i + 1), Title[i], Singer[i], Album[i]])

        file.close()

    def scrap(self):

        file = open("chart.csv", "w", newline="", encoding ="UTF-8")
        wr = csv.writer(file)
        wr.writerow(["Rank", "Title", "Singer", "Album"])
        file.close()

        Soup = self.getHTML()
        self.getchart(Soup)

if __name__ == "__main__" :
    s=Scraper()
    s.scrap()



