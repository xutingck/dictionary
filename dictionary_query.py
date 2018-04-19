#coding:utf-8

import MySQLdb, datetime

db = MySQLdb.connect(host = "localhost", user = "root", passwd = "001828", \
                     db = "dic", charset = "gbk")

cursor = db.cursor()

while True:
    startTime = datetime.datetime.now()
    print startTime
    wordInput = raw_input("word:")
    wordQuery = "select * from dic where ENG_CHS like '%" + wordInput + "%'"
    print wordQuery
    cursor.execute(wordQuery)

    results = cursor.fetchall()
    for row in results:
        print row[0], '->', row[1]

    print '-----------------------'
    
    

