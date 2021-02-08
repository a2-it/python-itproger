import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    #port = '6886' u can cange host in this way
    user = 'root',
    password = 'root',
    database = 'python-example'
)

myCur = mydb.cursor()
# sql = "CREATE DATABASE `python-example`"
# sql = "SHOW DATABASES"
# sql = "CREATE TABLE users (name VARCHAR(255), age INTEGER(3))"
# sql = "SHOW TABlES"
sql = " INSERT INTO articles (title, intro, date) VALUES(%s, %s, %s)"

articles = [('Larry Hotter', 'Volland', '2020-11-11'),
            ('Alice in W', 'SMBD', '2019-10-09'),
            ]
myCur.executemany(sql, articles) #принимает sql code и запускает
mydb.commit()


# for el in myCur: print(el)