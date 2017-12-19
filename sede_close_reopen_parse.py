#!/usr/bin/env python3

import mysql.connector, re, csv, datetime

db = mysql.connector.connect(user='dbuser', password='dbpass', database='worldbuilding')
cursor = db.cursor()   

cursor.execute("DROP TABLE IF EXISTS user_time, user_tag, user_reason;")
cursor.execute("CREATE TABLE user_time (userid INT, time DATETIME);")

with open("./worldbuilding_close_reopen_info.csv", 'r') as datain:
    csvin = csv.reader(datain)
    
    allusers = []
    
    for txt, creationtime, comment, tags, typeid in csvin:
        if int(typeid) == 10:
            users = re.findall('"Id":(\d+),', txt)
            t = datetime.datetime.strptime(creationtime, "%Y-%m-%d %H:%M:%S")
            allusers.extend([(u, t) for u in users])
            

    cursor.executemany("INSERT INTO user_time (userid, time) VALUES (%s, %s);", allusers)

db.commit()