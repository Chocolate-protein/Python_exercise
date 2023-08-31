# # Selenium 활용 - 구글 무비


import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US"
browser.get(url)
time.sleep(2)

# 지정한 위치로 스크롤 내리기 -> 자바 스크립트
# 모니터 (해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)")

# 화면 가장 아래로 스크롤 내리기
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2   # 2초에 한번씩 스크롤 내림

# 현재 문서 높이 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행(스크롤 내리기)
while True:
    # 스크롤 아래로 내리기
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # 페이지 로딩 대기
    time.sleep(interval)

    # 높이 갱신
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")



import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
   
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, " < 할인되지 않은 영화 제외 > ", end="\n\n")
        # print("-"*50, end="\n\n")
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = "https://play.google.com" + movie.find("a", attrs={"class":"JC71ub"})["href"]

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print(f"링크 : {link}", end="\n\n")
    print("-"*90, end="\n\n")


while True:
    pass