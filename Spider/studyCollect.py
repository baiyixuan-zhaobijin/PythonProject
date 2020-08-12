#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup
import pyperclip
url = 'https://www.cnblogs.com/ailiailan/tag/Python%E4%BB%A3%E7%A0%81%E7%9B%B8%E5%85%B3/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
data = soup.find_all(id='mainContent')
result = []
print(data)
for item in data:
    hrefs = item.find_all(class_='PostList')
    print(hrefs)
    for href in hrefs:
        title = href.find('span').text
        result.append(title)
result.reverse()
for item in result:
    print(item.strip())
