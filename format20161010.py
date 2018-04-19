#coding:utf-8

import datetime

StartTime = datetime.datetime.now()
print StartTime

file1 = open("C:\\Users\\xutin\\Desktop\\dictionary.txt","r")
file2 = open("C:\\Users\\xutin\\Desktop\\result.txt","r+")


while True:
    readline0 = file1.readline()
    if readline0 != "":
        string0 = readline0.replace("C11","INSERT INTO dic      VALUES ('")
        string0 = string0.replace("C22","','")
        string0 = string0.replace("C33"," -> ")
        string0 = string0.replace("C44","');")

        file2.write(string0)
    else:
        break

file1.close()
file2.close()

EndTime = datetime.datetime.now()
CostTime = EndTime - StartTime
print CostTime




