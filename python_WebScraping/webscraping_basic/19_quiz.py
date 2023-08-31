# quiz

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%8C%80%EC%A0%84+%ED%88%AC%EB%A3%B8"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

sales = soup.find_all("div", attrs={"class":"cont_place"})

for sale in sales:
    # 거래 종류
    type = sale.find("a", attrs={"class":"fn_tit"}).get_text()
    type = type[1:type.index("]")]

    # 가격
    price = sale.find("span", attrs={"class":"f_eb"})

    # 면적
    area = price.next_sibling.next_sibling.next_sibling.next_sibling

    # 층 수
    floor = area.next_sibling.next_sibling.next_sibling.next_sibling

    # 위치
    location = sale.find("div", attrs={"class":"info_more"}).find("span", attrs={"class":"f_eb"}).get_text()
    
    print("="*11, f"매물 {sales.index(sale)+1}", "="*11)
    print(f"거래 : {type}")
    print(f"면적 : {area.get_text()}")
    print(f"가격 : {price.get_text()}")
    print(f"층 : {floor.get_text()}")
    print(f"위치 : {location}")

