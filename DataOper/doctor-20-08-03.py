from peewee import *
import csv
import pandas as pd
fileName = 'D:\wamp64\www\PythonProject\DataOper\doctor.csv'
db = MySQLDatabase("doctor_exam", host="127.0.0.1", port=3306, user="root", passwd="123456")
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class doctors_test(BaseModel):
    name = CharField()
    province = CharField()
    city = CharField()
    hospital = CharField()
    department = CharField()
    job = CharField()

class doctors(BaseModel):
    name = CharField()
    hospital = CharField()
    telphone = CharField()
    department = CharField()

rlist  = []
n      = 0
with open(fileName) as f:
    reader   = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        result = []
        result.append(row[0])
        #result['province'] = row[1]
        #result['city'] = row[2]
        result.append(row[3])
        result.append(row[7])
        result.append(row[8])
        '''
        result['job'] = '4'
        if row[8].strip() == '主任医师':
            result['job']        = '5'
        elif row[8].strip() == '副主任医师':
            result['job']        = '2'
        elif row[8].strip() == '副主任医师 副教授':
            result['job']        = '2'
        elif row[8].strip() == '医师':
            result['job']        = '4'
        elif row[8].strip() == '主任医师 教授':
            result['job']        = '5'
        elif row[8].strip() == '主治医师':
            result['job']        = '1'
        elif row[8].strip() == '住院医师':
            result['job']        = '3'
        '''
        hospital = row[3]
        if hospital.find('(')>0:
            index = hospital.find('(')
            hospital = hospital[0:index]
        elif hospital.find('（')>0:
            index = hospital.find('（')
            hospital = hospital[0:index]
        if len(doctors.select().where(doctors.name == row[0],doctors.hospital == hospital)) > 0:
            doctor = doctors.get(doctors.name == row[0],doctors.hospital == hospital)

            result.append(str(doctor.telphone.strip()))
            result.append( str(doctor.department.strip()))
            #print(result)
            rlist.append(result)
           
            

    column = ['姓名','医院','执业范围','职称','电话','科室']
    test = pd.DataFrame(columns = column, data=rlist)
    test.to_csv('D:/test.csv') 
    print('任务完成')
