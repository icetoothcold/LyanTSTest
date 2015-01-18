__author__ = 'Lyan'
import sqlite3
conn=sqlite3.connect('test')
cursor=conn.cursor()
cursor.execute('create table user (id varchar(20) PRIMARY KEY ,name varchar(20))')

cursor.execute('INSERT INTO user (id,name) VALUES (?,?)',['1','Michael'])
print cursor.rowcount
conn.commit()
cursor.close()
conn.close()


