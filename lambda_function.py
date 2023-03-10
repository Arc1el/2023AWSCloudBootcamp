from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import boto3

def lambda_handler(event, context):
    # TODO implement
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

    chrome_options.binary_location = "/opt/python/bin/headless-chromium"
    driver = webdriver.Chrome('/opt/python/bin/chromedriver', chrome_options=chrome_options)
    print("driver arrive")
    
    driver.get("https://www.naver.com")
    
    sqs_client = boto3.client('sqs')
    msg = sqs_client.send_message(QueueUrl="", MessageBody='{"message" : "testmessage"}')
    print(msg)
    
    driver.close()
    
