# 11-1) 모듈
# 쓰려는 파일과 같은 경로에 있거나 
# 파이썬 라이브러리가 모여있는 폴더에 있어야 사용 가능
'''
import theater_module
theater_module.price(3)   # 3명이서 영화 관람 시 가격
theater_module.price_morning(4)   # 4명 조조영화 관람
theater_module.price_soldier(5)     # 5명 군인 영화 관람
'''

'''
import theater_module as mv  
# 파일에 별명을 붙이기 : theater_module -> mv 로 호출 가능
mv.price(3)     # == theater_module.price()
mv.price_morning(4)
mv.price_soldier(5)
'''

'''
from theater_module import *
# "theater_module." 필요없이 호출 가능
price(3)
price_morning(4)
price_soldier(5)
'''

'''
from theater_module import price, price_morning
# 특정함수만 가져올 수 있음
price(5)
price_morning(6)
# price_soldier(5)  : 오류
'''
'''
from theater_module import price_soldier as price
# : theater_module 의 price_soldier 함수에 price 라는 별명 붙여서 호출
price(5)
'''



# 11-2) 패키지 : 모듈들을 모아놓은 집합
'''
import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''
'''
from travel.japan import JapanPackage
trip_to = JapanPackage()
trip_to.detail()
'''
'''
from travel import thailand
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''



# 11-3) __all__  : __init__.py 참고
'''
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
'''



# 11-4) 모듈 직접 실행 -> thailand.py



# 11-5) 패키지, 모듈 위치
'''
from travel import *

import inspect
import random
print(inspect.getfile(random))   # random 파일의 위치 정보 출력
print(inspect.getfile(japan))
'''



# 11-6) pip install  : 이미 만들어져 있는 패키지 가져오기(다운)
# https://pypi.org/
# 위 사이트에서 필요한 패키지 찾은 후 터미널 창에 입력
# ex) pip install beautifulsoup4 : 설치
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
'''
# pip install package_name : 해당 패키지 설치
# pip list : 현재 저장되어있는 패키지 목록
# pip show package_name : 해당 패키지에 대한 내용 출력
# pip install --upgrade package_name : 패키지 업그레이드



# 11-7) 내장함수 : 따로 import 필요없이 바로 사용 가능
# input() : 사용자 입력 받는 함수
# dir : 객체를 넘겨줬을 때, 그 객체가 가지고 있는 변수, 함수 표시
'''
print(dir())
import random # 외장함수
print(dir())
import math
print(dir())
print(dir(random)) # : random 모듈 내에서 사용 가능한 것들 출력
'''
'''
lst = [1, 2, 3]
print(dir(lst))  # -> lst에 대해서 사용 가능한 것들 출력

name = "Kim"
print(dir(name))
'''
# https://docs.python.org/ko/3/library/functions.html
# : python 자체에서 사용 가능한 내장함수 제공



# 11-8) 외장함수
# https://docs.python.org/ko/3/py-modindex.html
# : python에서 제공되는 외장함수 목록

# ex) glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
'''
import glob
print(glob.glob("*.py"))  # 확장자가 py 인 모든 파일
'''

# ex) os : 운영체제에서 제공하는 기본 기능
'''
import os
print(os.getcwd())  # 현재 디렉토리 표시

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())
'''

# ex) time : 시간 관련 함수
'''
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
'''
'''
import datetime
print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 오늘 날짜로 부터 100일 후
print("지금으로부터 100일 후는", today + td)
'''