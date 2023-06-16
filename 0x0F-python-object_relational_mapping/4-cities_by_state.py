#!/usr/bin/python3
"""Lists all cities from the database"""

import MySQLdb as mysql
from sys import argv


if __name__ == '__main__':

    """
    Access the database and retrieve the list of cities.
    """
    db = mysql.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM cities JOIN states ON cities.state_id = states.id \
                   ORDER BY cities.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
