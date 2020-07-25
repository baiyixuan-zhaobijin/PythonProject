#招标数据采集  url: https://www.zbytb.com/
import re
import requests
from bs4 import BeautifulSoup
from peewee import *
import datetime
import time
import arrow
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
    html = soup.select('.neirong_m')
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

for i in range(1,6):
    url =  'https://www.zbytb.com/zb-{0}.html'.format(str(i))
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml') #lxml为解析器
    for idx, tr in enumerate(soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            area = tds[0].text.strip()
            project = tds[1].text.strip()
            link = tds[1].find('a').get('href').strip()
            publicTime = tds[3].text.strip()
            html = getContent(link)
            if link not in urlList:
                project_data.insert(
                companyId = 2,
                projectId = 2,
                projectRuleId = 4,
                title = '中国招标与采购网',
                listUrl = url,
                dataTitle = project,
                dataDay = publicTime,
                dataCategory = '',
                dataType = '',
                dataArea = area,
                detailUrl = link,
                detailContent = html,
                attachUrl = '',
                attachName = '',
                attachContent = '',
                attachId = '',
                status = 1,
                created_at = time.strftime('%Y-%m-%d %H:%M:%S')
            ).execute();
            time.sleep(1)

print('任务完成！')





