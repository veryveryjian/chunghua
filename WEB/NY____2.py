from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Google 계정 로그인 페이지로 이동
driver.get("https://accounts.google.com/")

# 로그인 절차 수행 (자동화 정책에 따라 이 부분은 실제 환경에서 사용에 주의가 필요합니다)
# 예시로, 이메일과 패스워드를 입력하고 로그인 버튼을 클릭하는 코드가 들어갈 수 있습니다.

# 사용자 정보 확인
try:
    user_info = driver.find_element_by_css_selector("a[href*='Account']").text
    print("Logged in user:", user_info)
except:
    print("No user is logged in or unable to retrieve user info.")

# 드라이버 종료
driver.quit()
