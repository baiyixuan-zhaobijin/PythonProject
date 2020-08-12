#coding:utf-8
import arrow
path = 'D:\\life\\日刊\\'
day = arrow.utcnow().to('local').format('YY-MM-DD')
time = arrow.utcnow().to('local').format('YY-MM-DD HH:mm:ss')
ftype = input()
typeList = {'1':'读书日刊','2':'英语日刊'}
fileName = path+str(day)+"·"+typeList[ftype]+".md"
fileList = {
    '1': "---\r\ntitle: 白衣轩读书日刊·{0}\r\ntags:\r\n  - 读书\r\ncategories:\r\n  - 白衣轩日刊\r\n  - 读书\r\nauthor: 赵碧金\r\ndate: {1}\r\n---".format(day,time)

}
with open(fileName,'w',encoding='utf-8') as f:
    f.write(fileList[ftype])

print('任务完成！')
