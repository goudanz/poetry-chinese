#!/usr/bin/python3

import pymysql

database = pymysql.connect("10.0.209.231", "gmdb", "PLrGisMS0HRaFE7f", "sstx477_log")

cursor = database.cursor()
cursor.execute("show databases like '%log';")
data = cursor.fetchall()

dbCnt = len(data);

for db in data:

    sql = "use " + db[0];
    cursor.execute(sql);

    cursor.execute("show tables;");
    tables = cursor.fetchall();

    tableName = tables[0][0];
    sql = "select count(*) as cnt from " + tableName;

    cursor.execute(sql);
    data = cursor.fetchall();

    msg = "数据库：" + db[0] + "-表：" + tableName + " 有：" + str(data[0][0]) + "条";

    print(msg)


database.close()




