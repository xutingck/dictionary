#coding:utf-8
import MySQLdb, datetime, sys

timeStart = datetime.datetime.now()

print timeStart


db = MySQLdb.connect(host = "localhost",user= "root",passwd = "001828",db = "dic", charset = "utf8")

cursor = db.cursor()


DicSql = open("C:\\Users\\xutin\\Desktop\\dic1.txt",'r')

try:
    while True:
        readDicSql = DicSql.readline()
        print readDicSql

        readDicSql1= readDicSql.replace('\xef\xbb\xbf', '')
        cursor.execute(readDicSql1)
        db.commit()
except EOFError:
    pass
except:
    print "Something other happens..."

db.close()

timeEnd = datetime.datetime.now()

print timeEnd

timeCost = timeEnd - timeStart

print timeCost
