import warnings
from unicodedata import category
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import numpy as np

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
    url = item.select_one("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div > a")["href"]
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
            stack = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(11)").get_text()
            endDate = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(1) > span.body").get_text()
            location = soup.select_one("div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(2) > span.body").get_text()
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
            temp.append(stack)
            temp.append(endDate)
            datas.append(temp)
            
        

print("Data Length : " + str(len(datas)))

# convert python array -> numpy array -> pandas dataframe
datas_narray = np.array(datas)
dataframe = pd.DataFrame(datas_narray)

# rename columns
dataframe.columns = ["회사명", "위치", "포지션", "회사소개", "주요업무", "자격요견", "우대사항", "혜택 및 복지", "기술스택", "마감일"]

# save dataframe to csv using utf-8 encording
dataframe.to_csv("data.csv", mode='w', encoding="utf-8-sig")