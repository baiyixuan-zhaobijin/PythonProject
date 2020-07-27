# 二手车数据爬取
#coding:utf-8
import re
import requests
from bs4 import BeautifulSoup
from peewee import *
import datetime
import time
import arrow
import json
db = MySQLDatabase("test", host="127.0.0.1", port=3306, user="root", passwd="123456")
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class project_data_car(BaseModel):
    title      = CharField()
    age        = IntegerField()
    distance   = DecimalField()
    price      = DecimalField()
    merchant   = CharField()
    mtype      = CharField()
    buyDate    = CharField()
    detailUrl  = CharField()
    carType    = CharField()
    remark     = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

#鸡西百姓网
def getBaixing(url,urlList):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find_all(class_ = ['listing-ad','item-regular','seen'])
    result = {}
    for idx, item in enumerate(data):
        if idx != 0:
            href = item.find(class_ = ['ad-title'])['href']
            if href not in urlList:
                result['carType']   = item.find(class_ = ['tag','tag-category']).text.strip()
                result['title']     = item.find(class_ = ['ad-title']).text.strip()
                price               = str(item.find(class_ = ['highlight']).text.strip())
                if price[:-2] is '':
                    result['price']     = 0
                else:
                    result['price']     = price[:-2]
                result['merchant']  = item.find(class_ = ['ad-item-detail']).text.strip()
                content             = item.find(class_ = ['ad-item-detail']).find_next_sibling().text.strip()
                content_list        = content.split('/')
                if content_list[0].find('更新')<0:
                    result['mtype']     = content_list[0]
                if len(content_list)>1 and content_list[1].find('年')>=0 : 
                    result['buyDate'] = content_list[1]
                if len(content_list)>2 and content_list[2].find('公里')>=0:
                    distance =  str(content_list[2]).strip()
                    result['distance'] = distance[:-4]
                result['detailUrl']    = href
                project_data_car.insert(result).execute()
#鸡西58同城
def getTongcheng(url,urlList):
    r   = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find_all(class_ = ['info--desc'])
    result = {}
    for idx, item in enumerate(data):
        if idx != 0:
            result['title'] = item.find(class_='info_link')
#鸡西赶集网
def getGanji(url,urlList):
    r   = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.find_all(class_ = ['list-pic','clearfix','cursor_pointer'])
    result = {}
    for idx, item in enumerate(data):
        if idx != 0:
            result['title'] = item.find(class_=['infor-title','pt_tit','js-title'])
            print(result)
print(soup)

'''
urlList = []
for url in project_data_car.select(project_data_car.detailUrl):
    urlList.append(url.detailUrl)
'''
for i in range(1,1):
    #url = 'https://jixi.baixing.com/cheliang/?page=%d'.format(i)
    #getBaixing(url,urlList)
    #url = 'https://jixi.58.com/ershouche/pn%d/?PGTID=0d100000-01c7-92a6-616f-3afaed1bae9c&ClickID=57'.format(i)
    #getTongcheng(url,'')
    url = 'http://jixi.ganji.com/ershouche/o2/'
    getGanji(url,'')



print('任务完成！')
       

