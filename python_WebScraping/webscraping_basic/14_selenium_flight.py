# Selenium 활용1 - 네이버 항공권

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()   # 전체화면 모드

url = "https://flight.naver.com/"
browser.get(url)   # url 로 이동
''''''
# 가는 날 선택 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
time.sleep(1)

# 이번 달 27일, 다음 달 28일 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[7]/button").click()

# 도착지 선택 : 일본 - 오사카
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/button[2]").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div[2]/section/section/div/button[1]").click()

# 직항만 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[3]/button[2]").click()
time.sleep(1)

# 항공권 검색 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()

# 로딩 화면 대기
try:
    ele = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]/div/button")))
    print(ele.text)    # 첫번째 결과 출력
finally:
    # browser.quit()
    pass

# # 첫번째 결과 출력
# ele = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]/div/button")
# print(ele.text)



while True:
    pass