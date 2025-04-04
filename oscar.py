import mysql.connector

cnx = mysql.connector.connect(
    user='root', 
    password='mysql',
    host='127.0.0.1', 
    database='oscar_dijas_filmek'
)
cursor = cnx.cursor()

cursor.execute("""SELECT cim, ev FROM film 
               WHERE nyert = 1 ORDER BY ev;""")
print("2. Az elnyerés éve és a film eredeti címe")
for sorok in cursor.fetchall():
    print(sorok)

cursor.close()
cnx.close()