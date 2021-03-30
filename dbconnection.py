import sqlite3
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute(
    'create table if not exists USERS(id INTEGER PRIMARY KEY AUTOINCREMENT ,username text,password text)')

cur.execute(
    ' create table if not exists BOOKS(ISBN TEXT PRIMARY KEY,AUTHOR TEXT,NAME TEXT,QUANTITY INTEGER)')

con.close()
