#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. Safe from MySQL injections!
"""

import MySQLdb as mysql
from sys import argv


if __name__ == '__main__':

    """
    Access the database and retrieve the states.
    """
    db = mysql.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC", {'name': argv[4]})

    rows = cursor.fetchall()

    for row in rows:
        print(row)
