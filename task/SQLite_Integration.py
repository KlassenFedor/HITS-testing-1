import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


new_connection = create_connection("./my_db.db")

cur = new_connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS answers(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   input_number INTEGER, 
   value TEXT);
""")
new_connection.commit()
