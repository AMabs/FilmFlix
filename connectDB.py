import sqlite3 as sql

conn = sql.connect("filmflix.db")

cursor = conn.cursor()