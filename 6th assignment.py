from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/chromedriver"

searchIndex = input("원하는 검색어 입력하세요:")
driver = webdriver.Chrome(path)

try:
    driver.get('https://www.youtube.com/?hl=ko&gl=KR&app=desktop')

    element = driver.find_element_by_class_name('style-scope ytd-searchbox')

    element.send_keys(searchIndex)

    driver.find_element_by_xpath(
        "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button").click()

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    all_title = soup.find_all('h3', class_ ='title-and-badge style-scope ytd-video-renderer')
    print(all_title)
    title = [soup.find_all('h3', class_='title-and-badge style-scope ytd-video-renderer')[n].string for n in
             range(0, len(all_title))]

    print(title)

finally :
    time.sleep(3)

    driver.quit()
