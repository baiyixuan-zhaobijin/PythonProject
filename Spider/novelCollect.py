# 小说爬取
#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup
import pyperclip
#眠月魔情录
#title='眠月魔情录'
#url = 'https://www.jupindai.com/book/42200.html'
title = '枭臣'
url = 'https://www.jupindai.com/book/25512.html'
r = requests.get(url)
r.encoding = 'GBK'

soup = BeautifulSoup(r.text, 'lxml')

data = soup.find_all(id ="list-chapterAll")
result = []
chapter={}
for item in data:
    hrefs = item.find_all('a')
    for href in hrefs:
        if href['href'] != 'javascript:;':
            chapter['name'] = href.text
            chapter['href'] = href['href']
            result.append(chapter)
            chapter={}
            

n=1
str1 = '#### '+title+'\r\n'
for item in result:
    str1 = str1+'- [ ] '+str(n)+'. 【 】第'+str(n)+'章:['+item['name']+'](https://www.jupindai.com'+item['href'] +')'+'\r\n'
    n = n+1
    print(item['name'])
pyperclip.copy(str1)