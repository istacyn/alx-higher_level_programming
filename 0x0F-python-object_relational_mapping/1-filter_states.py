#!/usr/bin/python3
"""Lists all states from the database"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    """
    Access the database and retrieve the list of states starting with N.
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2],
        database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states
                   WHERE name LIKE 'N%' ORDER BY states.id in ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
