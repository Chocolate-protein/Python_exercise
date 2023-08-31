# BeautifulSoup4 활용 - 다음 이미지(영화)

import requests
from bs4 import BeautifulSoup

for year in range(2016, 2022):

    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url) 
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})
        
    for idx, img in enumerate(images):
        img_url = img["src"]
        if img_url.startswith("//"):   # // 로 시작하는 문자열
            img_url = "https:" + img_url
        
        print(img_url)
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open("movie{0}-{1}.jpg".format(year, idx + 1), "wb") as f:
            f.write(img_res.content)
        
        if idx >= 4:   # 상위 5개 이미지까지만 다운로드
            break