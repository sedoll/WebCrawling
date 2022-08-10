from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 매니저를 통해 크롬 최신버전 설치하고 객체 생성
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 웹페이지 주소 이동
driver.get("https://www.naver.com")