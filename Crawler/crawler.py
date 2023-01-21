from unicodedata import category
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Initialize Crawler
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.implicitly_wait(3)

url = "https://www.wanted.co.kr/wdlist?country=kr&job_sort=company.response_rate_order&years=-1&locations=all"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
items = soup.select("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div")

#result = []
urls = []
for item in items:
    temp = []
    url = item.select_one("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div > a")["href"]
    #companyName = item.select_one("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div > a")["data-company-name"]
    #category = item.select_one("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div > a")["data-job-category"]
    #position = item.select_one("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div > a")["data-position-name"]
    temp.append("https://wanted.co.kr" + url)
    #temp.append(companyName)
    #temp.append(category)
    #temp.append(position)
    
    # result.append(temp)
    urls.append(temp)
    # print(temp)
    
print(urls)
#print(items)
