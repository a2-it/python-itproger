import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    #port = '6886' u can cange host in this way
    user = 'root',
    password = 'root',
    database = 'itprogerhw'
)
myCur = mydb.cursor()
sql0 = "TRUNCATE orders"
myCur.execute(sql0)
sql0 = "INSERT INTO orders (userid, itemid) VALUES (%s, %s)"
myCur.execute(sql0, (1,3))
myCur.execute(sql0, (1,2))
mydb.commit()

#somechanges
sql0 = "SELECT CONCAT(users.login, '  -  ', items.title) AS 'ВСЕ ЗАКАЗЫ' FROM orders JOIN users ON users.id = orders.userid JOIN items on items.id = orders.itemid"
myCur.execute(sql0)
result = myCur.fetchall()
print('Все заказы\n\n')
for el in result:
    for i in el:
        print(i)