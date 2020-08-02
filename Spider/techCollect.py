#科技周刊 数据爬取
#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup

url = 'http://www.ruanyifeng.com/blog/2018/04/weekly-issue-1.html'
r = requests.get(url)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'lxml')
data = soup.find_all(id="main-content")
list1 = ['','个人网站','微信公众号','语雀','']
uniqeList = []
for item in data:
    hrefs = item.find_all('a')
    for href in hrefs:
        if href.text not in list1 and href['href'] not in uniqeList:
            print('['+href.text+']('+href['href']+")")
            uniqeList.append(href['href'])
