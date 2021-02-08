import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    #port = '6886' u can cange host in this way
    user = 'root',
    password = 'root',
    database = 'python-example'
)

myCur = mydb.cursor()

sql = "SELECT * FROM articles WHERE id<4 ORDER BY title DESC"
#сортируем по айди по возрастанию ASC, убыванию DESC
myCur.execute(sql)
res = myCur.fetchall()
print(res)

sql1 = "SELECT id, date FROM articles LIMIT 2"
#LIMIT на аутпут записей
myCur.execute(sql1)
res = myCur.fetchall()
print(res)

sql2 = "SELECT id, date FROM articles LIMIT 2 OFFSET 2"
#LIMIT на аутпут записей, выводит пропуская первые 2
myCur.execute(sql2)
res = myCur.fetchall()
print(res)

