#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb as mysql
from sys import argv


if __name__ == '__main__':

    """
    Access the database and retrieve the list of cities.
    """
    db = mysql.connect(host="localhost", port=3306,
                       user=argv[1], passwd=argv[2], database=argv[3])

    with db.cursor() as cursor:
        cursor.execute("""
            SELECT cities.id, cities.name
            FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %(state_name)s
            ORDER BY cities.id ASC
        """, {
            'state_name:': argv[4]
        })

        rows = cursor.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
