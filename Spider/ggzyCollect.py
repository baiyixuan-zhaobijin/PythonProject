#全国公共资源交易平台  url: http://deal.ggzy.gov.cn/ds/deal/dealList.jsp
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

class project_data(BaseModel):
    companyId = IntegerField()
    projectId = IntegerField()
    projectRuleId = IntegerField()
    title = CharField()
    listUrl = CharField()
    dataTitle = CharField()
    dataDay = DateTimeField()
    dataCategory = CharField()
    dataType = CharField()
    dataArea = CharField()
    detailUrl = CharField()
    detailContent = CharField()
    attachUrl = CharField()
    attachName = CharField()
    createTime = DateTimeField()
    attachContent = CharField()
    attachId = CharField()
    status = IntegerField()
    uid = IntegerField()
    updateTime = DateTimeField()
    selectGroup = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

def getContent(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    html = soup.select('.fully')
    if (len(html)):
        return html[0]
    else:
        return '';

#删除数据
yesterday = arrow.utcnow().shift(days=-1).format('YYYY-MM-DD')
project_data.delete().where(project_data.dataDay<yesterday).execute()

urlList = []
for url in project_data.select(project_data.detailUrl):
    urlList.append(url.detailUrl)

today = arrow.utcnow().format('YYYY-MM-DD')
before = arrow.utcnow().shift(days=-9).format('YYYY-MM-DD')
url = 'http://deal.ggzy.gov.cn/ds/deal/dealList_find.jsp'
for n in range(1,6):
    postData = {
    'TIMEBEGIN_SHOW': before,
    'TIMEEND_SHOW'  : today,
    'TIMEBEGIN'     : before,
    'TIMEEND'       : today,
    'SOURCE_TYPE'   : 1,
    'DEAL_TIME'     : '02',
    'DEAL_CLASSIFY' : '00',
    'DEAL_STAGE'    : '0000',
    'DEAL_PROVINCE' : 0,
    'DEAL_CITY'     : 0,
    'DEAL_PLATFORM' : 0,
    'BID_PLATFORM'  : 0,
    'DEAL_TRADE'    : 0,
    'isShowAll'     : 1,
    'PAGENUMBER'    : n,
    'FINDTXT'       : ''
}
    res = requests.post(url=url,data=postData)
    data =  json.loads(res.text.strip())
    for item in data['data']:
        if item['url'].strip() not in urlList:
            project_data.insert(
                        companyId = 2,
                        projectId = 2,
                        projectRuleId = 4,
                        title = '全国公共资源交易平台',
                        listUrl = url,
                        dataTitle = item['title'].strip(),
                        dataDay = item['timeShow'].strip(),
                        dataCategory = item['classifyShow'].strip(),
                        dataType = item['stageShow'].strip(),
                        dataArea = item['districtShow'].strip(),
                        detailUrl = item['url'].strip(),
                        detailContent = getContent(item['url'].strip()),
                        attachUrl = '',
                        attachName = '',
                        attachContent = '',
                        attachId = '',
                        status = 1,
                        created_at = time.strftime('%Y-%m-%d %H:%M:%S')
                    ).execute();
    time.sleep(5)

print('任务完成！')





