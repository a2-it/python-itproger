import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    #port = '6886' u can cange host in this way
    user = 'root',
    password = 'root',
    database = 'python-example'
)
myCur = mydb.cursor()
sql0 = "UPDATE articles SET title = %s WHERE id = %s"
myCur.execute(sql0, ('Updates Harry', 3))
mydb.commit()


sql2 = "DElETE FROM articles WHERE id = %s"
myCur.execute(sql2,(3,))
mydb.commit()

sql3 = "SELECT * FROM articles"
myCur.execute(sql3)
res = myCur.fetchall()
for el in res:
    print(res)