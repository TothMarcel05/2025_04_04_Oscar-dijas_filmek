import mysql.connector

cnx = mysql.connector.connect(
    user='root', password='your_password_here', host='127.0.0.1', database='oscar_dijas_filmek'
)
cursor = cnx.cursor()
cursor.execute("""
    SELECT ev, eredeti_cim 
    FROM film 
    ORDER BY ev;
""")
print("\n2:")
for row in cursor:
    print(row)

# 3. Years with at least 10 nominated films
cursor.execute("""
    SELECT jelolesev 
    FROM film 
    GROUP BY jelolesev 
    HAVING COUNT(*) >= 10;
""")
print("\n3:")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT eredeti_cim 
    FROM film 
    WHERE jelolesev BETWEEN 1939 AND 1945 AND bemutato_hu BETWEEN 1939 AND 1945;
""")
print("\n4:")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT eredeti_cim 
    FROM film 
    WHERE bemutato_hu >= ev + 10;
""")
print("\n5:")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT producer, COUNT(*), MAX(jelolesev) - MIN(jelolesev) AS ev_tavolsag 
    FROM film_producer 
    GROUP BY producer 
    HAVING COUNT(*) > 1;
""")

print("\n6:")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT DISTINCT producer 
    FROM film_producer 
    WHERE film_id IN (SELECT film_id FROM film_producer WHERE producer = 'Clint Eastwood') 
    AND producer <> 'Clint Eastwood';
""")
print("\n7:")
for row in cursor:
    print(row)


cursor.execute("""
    SELECT DISTINCT fp.producer 
    FROM film_producer fp 
    JOIN film f ON fp.film_id = f.id 
    WHERE f.bemutato_hu IS NULL 
    GROUP BY fp.producer 
    HAVING COUNT(*) = (SELECT COUNT(*) FROM film_producer WHERE producer = fp.producer);
""")
print("\n8:")
for row in cursor:
    print(row)

cursor.close()
cnx.close()
