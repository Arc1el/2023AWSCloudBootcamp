import warnings
from unicodedata import category
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import time
import pandas as pd
import numpy as np
import requests

"""
# ignore warning message
warnings.filterwarnings("ignore")

# Initialize Crawler
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.implicitly_wait(3)

# crawling target(1)
url = "https://www.wanted.co.kr/wdlist?country=kr&job_sort=company.response_rate_order&years=-1&locations=all"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
items = soup.select("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div")

# datas(1)
urls = []
for item in items:
    url = item.select_one("a")["href"]
    urls.append("https://wanted.co.kr" + url) 
    
print("Urls : ")
print(urls)
print()

datas = []
for url in urls:
    
    # crawling target(2)
    driver.get(url)
    #driver.implicitly_wait(30)
    sleep(1)
    
    # for dynamic contents, scroll the page 0 to 3500
    driver.execute_script('window.scrollTo(0, 500);');sleep(0.3);driver.execute_script('window.scrollTo(500, 1000);');sleep(0.3)
    driver.execute_script('window.scrollTo(1000, 1500);');sleep(0.3);driver.execute_script('window.scrollTo(1500, 2000);');sleep(0.3)
    driver.execute_script('window.scrollTo(2000, 2500);');sleep(0.3);driver.execute_script('window.scrollTo(2500, 3000);');sleep(0.3)
    driver.execute_script('window.scrollTo(3000, 3500);');sleep(0.3);driver.execute_script('window.scrollTo(3500, 4000);');sleep(1)
    
    # scroll to the div that location and endDate data exist
    try:
        element = driver.find_element(By.CSS_SELECTOR, "#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp")
        location = element.location_once_scrolled_into_view
        driver.execute_script('arguments[0].scrollIntoView(true);', element)
        sleep(2)
    except:
        pass

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select("#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div.JobContent_className___ca57")
    for item in items:
        temp = []
        # for missing value
        name, position, description, task, qualifications, prefer, welfare, stack, endDate, location = "","","","","","","","","",""
        try:
            # get data
            name = item.select_one("section.JobHeader_className__HttDA > div:nth-child(2) > h6 > a").get_text()
            description = item.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(1) > span").get_text()
            position = soup.select_one("section.JobHeader_className__HttDA > h2").get_text()
            task = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section > p:nth-child(3)").get_text()
            qualifications = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section > p:nth-child(5)").get_text()
            prefer = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(7)").get_text()
            welfare = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(9)").get_text()
            endDate = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(1) > span.body").get_text()
            location = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(2) > span.body").get_text()
            stack = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(11)").get_text()
        except:
            pass
        finally:
            # append to datas
            temp.append(name)
            temp.append(location)
            temp.append(position)
            temp.append(description)
            temp.append(task)
            temp.append(qualifications)
            temp.append(prefer)
            temp.append(welfare)
            temp.append(endDate)
            temp.append(stack)
            datas.append(temp)
            
print("Data Length : " + str(len(datas)))

# convert python array -> numpy array -> pandas dataframe
datas_narray = np.array(datas)
dataframe = pd.DataFrame(datas_narray)

# rename columns
dataframe.columns = ["회사명", "위치", "포지션", "회사소개", "주요업무", "자격요견", "우대사항", "혜택 및 복지", "마감일", "기술스택"]

# save dataframe to csv using utf-8 encording
dataframe.to_csv("data.csv", mode='w', encoding="utf-8-sig")
"""

# send request to slack app-server
# example data
datas = [
    {
        "title" : "스윗코리아",
        "location" : "서울시 강남구 삼성로 570",
        "description" : "[스윗소개]스윗테크놀로지스는 미국 실리콘밸리에 본사를 둔 글로벌 테크 스타트업입니다. 채팅과 업무관리를 결합한 Swit은 'Google Workspace'나 'MS Office365' 'Zoom'등의 업무 필수 앱들과 완벽히 연동되고 전자결재, 프로젝트 관리등의 협업 기능등을 한곳에 모은 플랫폼으로, 단일 기능을 제공하던 기존 협업툴과는 다른 협업 운영체제 입니다. 스윗은 이런 차별화를 바탕으로 2019년 정식 버전 출시이래  글로벌 협업툴로 빠르게 성장하고 있습니다.또한 시리즈A 투자유치를 성공적으로 진행하며, 우수 인재분들을 채용 중에 있습니다. 글로벌 서비스를 함께 만들어갈 실력있는 예비 Switter분들의 지원을 기다립니다[합류 여정]• 1차 서류제출 → 코딩TEST → 2차 직무인터뷰(Online) → 3차 컬쳐핏인터뷰(Offline) → 처우협의/최종합격 → 입사- 해당공고는 수시채용으로, 우수인재 채용 완료시 조기에 마감될수 있습니다 - 각 전형 결과 안내는 모든 지원자분들에게 개별적으로 메일을 통해 안내해드리고 있습니다.- 지원자분의 이력 및 경력 사항에 따라 일부 전형 과정이 생략되거나 추가될 수 있습니다.- 수습기간 3개월[제출서류]• 경력 중심의 이력서 (필수) ※PDF파일 • 포트폴리오 (링크, 파일첨부 모두 가능)",
        "position" : "백엔드 개발자 Backend Developer (3년이상)",
        "startDate" : "20230122T130000",
        "endDate" : "20230122T170000",
        "timestamp" : time.time()
    },
    {
        "title" : "에이시티게임즈",
        "location" : "강남구 삼성로 99길 11 (곰비빌딩)",
        "description" : "에이시티 게임즈는 2019년 IP 전문 게임 개발 회사로 시작하여 IP를 활용한 5개의 게임을 성공적으로 개발/운영하고 있으며 새로운 IP발굴 및 확장을 지속적으로 진행하고 있습니다. 블록체인 기반의 P2E게임인 ZOIDS NFT ARENA 경우 지난달 11월 프론티어 테스트를 진행하였고 내년 정식 런칭을 예정중에 있습니다. 리니지,서든어택,피파온라인,킹덤오브히어로 등 유수한 게임 개발/운영에 참여한 평균 경력 16년 이상의 개발팀이 글로벌 서비스를 운영하고 있습니다. 2023년 미국과 프랑스를 포함한 글로벌 지사 런칭 예정이며,  Web3 마켓을 선도하는 게임 개발사로 자리매김 하고있는 여정에 시너지를 낼 수 있는 동료를 찾고 있습니다.저희는 Web3 시장을 개척하고 선점하는 도전을 해내고 있습니다. 이를 위해 기민하고 탄탄한 전문가들이 모여 새로운 것들을 시도하고 솔루션을 찾아내는 조직입니다 :)아래와 같은 역량과 태도를 갖춘 분이라면 저희와 좋은 시너지를 낼 수 있을거에요!• 스스로 최고의 기준을 설정하고 달성하는 전문성(Professionalism)• 문제를 정의하고 돌파하는 집요함(Problem Solving)과 열정(Enthusiasm)• 정확하게 소통하고 넓게 공유하며 동료들과 효과적으로 협업하는 태도 (Communication & Collaboration)",
        "position" : "Web3 사업개발(BD)",
        "startDate" : "20230123T130000",
        "endDate" : "20230123T170000",
        "timestamp" : time.time()
    }
]

slackAppUrl = "http://server.arc1el.kr:2222/slack/sendMessage"
headers = {"Content-Type" : "application/json; charset=utf-8"}
response = requests.post(slackAppUrl, json=datas, headers=headers)
print(response)