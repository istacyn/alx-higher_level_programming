#!/usr/bin/python3
"""Lists all states from the database starting with 'N'"""

import MySQLdb as mysql
from sys import argv


if __name__ == '__main__':

    """
    Access the database and retrieve the list of states starting with N.
    """
    db = mysql.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                   ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
