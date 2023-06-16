#!/usr/bin/python3
"""Lists all states from the database"""

import MySQLdb
from sys import argv


"""Access the database and retrieve the list of states"""
db_connection = MySQLdb.connect(
    host="localhost",
    user=argv[1],
    port=3306,
    passwd=argv[2]
    database=argv[3]
)

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM states")

result = cursor.fetchall()

for row in result:
    print(row)
