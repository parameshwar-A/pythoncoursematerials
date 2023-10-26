import sqlite3

# Creates a connection with the db.
my_conn = sqlite3.connect("mydb.db")

# Cursor is a pointer in our OS. But it points to a location in db
cur = my_conn.cursor()

# Cursors are used to execute SQL statements.
# cur.execute(""" 
# CREATE TABLE cars(
#     name text,
#     type text,
#     engine_cc real
#     )""")

# Commit is a concept in databases. It simply means save the db
# my_conn.commit()


# Closing the db connection properly.
# my_conn.close()


# CRUD operations
# CRUD are operated by simple changes in command only. Otherwise all statements are executed by execute mehtod of cursor. 
# Just we have some format specifiers in this lib.

# CREATE
# cur.execute("INSERT INTO cars VALUES ('i10', 'hatchback', 1.2 )")
# cur.execute("INSERT INTO cars VALUES ('Xylo', 'SUV', 1.5 )")


# READ
# cur.execute("SELECT name from cars WHERE engine_cc>1.3")
# print(cur.fetchall())

# You have three options fetchone, fetchmany, fetchall.

# UPDATE
# cur.execute("UPDATE cars SET engine_cc = 1.8 where engine_cc > 1.3")
# seccur = my_conn.cursor()
# seccur.execute("SELECT * from cars")
# print(seccur.fetchall())

# DELETE
# cur.execute("DELETE FROM cars WHERE engine_cc<1.3")
# seccur.execute("SELECT * from cars")
# print(seccur.fetchall())


# my_conn.commit()
# my_conn.close()
