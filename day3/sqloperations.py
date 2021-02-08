import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    #port = '6886' u can cange host in this way
    user = 'root',
    password = 'root',
    database = 'python-example'
)

myCur = mydb.cursor()
#sql = "SELECT * FROM articles"
#SELECT id, date FROM aricles
#SELECT * FROM article WHERE id = 3   // id>3  //<> значит не равно
#SELECT * FROM article WHERE title = 'Harry Potter' //
#SELECT * FROM article WHERE title LIKE 'Harry' ..статьи со соловом 'Harry'
#SELECT * FROM article WHERE title LIKE '%a% // все статьи с буквой 'a'
#SELECT * FROM article WHERE title NOT LIKE '%4% AND id > 2 //без буквы 4 и айди больще 2
#SELECT * FROM article WHERE title NOT LIKE '%4% OR id > 2 //без буквы 4 или айди больще 2
sql = "SELECT * FROM articles WHERE title NOT LIKE '%s%' OR id < 4"
myCur.execute(sql,(4,))

res = myCur.fetchall()
#res = myCur.fetchone()если хочу вывести только одну запись
for el in res:
    print(el)