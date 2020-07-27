import arrow
from bs4 import BeautifulSoup
from peewee import *
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
url = 'https://jixi.58.com/ershouche/pn1/?PGTID=0d100000-01c7-92a6-616f-3afaed1bae9c&ClickID=57'
url = 'http://jixi.ganji.com/ershouche/'
url = 'https://jixi.58.com/ershouche/pn1/?PGTID=0d100000-01c7-92a6-616f-3afaed1bae9c&ClickID=57'
       
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36' }
headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection' : 'Keep-Alive',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'Cookie':'commontopbar_new_city_info=7289%7C%E9%B8%A1%E8%A5%BF%7Cjixi; commontopbar_ipcity=sh%7C%E4%B8%8A%E6%B5%B7%7C0; userid360_xml=1461457F3DDCE2E376AE3C404176B698; time_create=1598415166196; f=n; id58=c5/nfF8eVDxIH2AqR4q8Ag==; 58tj_uuid=8a001124-f273-4232-9d76-e9d12f75f837; als=0; wmda_uuid=45badebbb4bd3a45a1a2620417588633; wmda_new_uuid=1; 58home=sh; city=sh; wmda_visited_projects=%3B1732038237441%3B11187958619315; xxzl_deviceid=DqpbHmDntVy%2FtdSsIC4X4nnCLgRYa34lbaGZ9HKsuF%2FTAIzA82q0sPebjb%2Blg2P3; new_uv=2; utm_source=; spm=; init_refer=; wmda_session_id_1732038237441=1595827329085-bc2f8abb-2b60-ea86; new_session=0; xxzl_cid=34b8bd2e8dc14f17abb65822a14d107a; xzuid=30c9744c-24dc-447d-a627-12439ea72de0; sessionid=368ed379-1cc0-4cd1-a676-8d1b89a79154; f=n',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
'''
driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.get(url)
instance = WebDriverWait(driver,9000).until(EC.presence_of_element_located((By.ID,'nav')))
print(instance.text)
driver.quit()

'''
params = {
  'PGTID' : '0d100000-01c7-92a6-616f-3afaed1bae9c',
  'ClickID' : '57'
}
r   = requests.get(url,params,headers=headers)
soup = BeautifulSoup(r.text, 'lxml',from_encoding="utf-8")
data = soup.find(class_ = 'info--pics')
print(data.text)






'''
str = '别克 / 2005年04月 / 14万公里 / 凯越 / 15分钟前更新'
content_list = str.split('/')
if len(content_list)>1 and content_list[1].find('年')>=0 : 
    print(content_list[1])
if len(content_list)>2 and content_list[2].find('公里')>=0:
     print(content_list[2][:-4])
'''