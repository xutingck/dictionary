#coding:utf-8

import MySQLdb, datetime, sys

timeStart = datetime.datetime.now()

print timeStart


db = MySQLdb.connect(host = "localhost",user= "root",passwd = "001828",db = "dic", charset = "utf8")

cursor = db.cursor()


DicSql = open("C:\\Users\\xutin\\Desktop\\result.txt",'r')

while True:
    readDicSql = DicSql.readline()
    if readDicSql != "":
        print readDicSql

        readDicSql1= readDicSql.replace('\xef\xbb\xbf', '')
        cursor.execute(readDicSql1)
        db.commit()
    else:
        break

db.close()

timeEnd = datetime.datetime.now()

print timeEnd

timeCost = timeEnd - timeStart

print timeCost
