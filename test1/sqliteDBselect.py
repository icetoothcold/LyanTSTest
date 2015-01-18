__author__ = 'Lyan'
import sqlite3
conn=sqlite3.connect('test')
cursor=conn.cursor()
cursor.execute('select * from user ')
print cursor.fetchall()
cursor.close()
conn.close()

