# Selenium 기본

import time
from selenium import webdriver

browser = webdriver.Chrome()   # 소스코드와 다른 경로에 있을 경우 경로 입력해야함

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼
elem = browser.find_element_by_class_name("link_login")
elem.click()


# 3. id, password 입력
browser.find_element_by_id("id").send_keys("naver_id")

time.sleep(3)

browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. 로그인 실패 시 id 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("password")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close()   # 현재 탭 종료
browser.quit()    # 브라우저 전체 종료

while True:
    pass