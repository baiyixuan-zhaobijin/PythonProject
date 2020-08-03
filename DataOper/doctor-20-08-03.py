from peewee import *
import csv
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

result = {}
with open(fileName) as f:
    reader   = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        result['name'] = row[0]
        result['province'] = row[1]
        result['city'] = row[2]
        result['hospital']   = row[3]
        result['department'] = row[7]
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
        if len(doctors.select().where(doctors.name == row[0],doctors.hospital == row[3])) == 0:
            doctors_test.insert(result).execute()
            print(result)