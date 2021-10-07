"""
Calling SQL code from Python
(executa cod SQL din Python, SQL queries)
metoda .execute(SQL_query)
Datatypes: https://www.sqlite.org/datatype3.html
text, integer, real, null, blob
Comenzi SQLite: https://www.sqlite.org/lang.html

"""

import sqlite3

# cream o conexiune la baza de date
con = sqlite3.connect('curs.db')

# cream un cursor

cursor = con.cursor()

# executam SQL queries (interogari SQL)
comanda_SQL = """CREATE TABLE IF NOT EXISTS studenti(
    nume text,
    curs text,
    lectie integer
)"""
cursor.execute(comanda_SQL)
# comanda2 = """INSERT INTO studenti VALUES(
#     'John Doe',
#     'Python Developer',
#     8)"""
# cursor.execute(comanda2)
# cursor.execute("""INSERT INTO studenti VALUES(
#     'Max Doe',
#     'Python Developer',
#     6)""")
cursor.execute("SELECT * FROM studenti")
results = cursor.fetchall()
# print(results)
for row in results:
    print(row)
con.commit()
con.close()
