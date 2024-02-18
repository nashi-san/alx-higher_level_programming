#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )
    cur = db.cursor()

    query = "SELECT cities.name \
            FROM cities INNER JOIN states ON \
            cities.state_id = states.id WHERE \
            states.name = %s ORDER BY cities.id"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    result = ", ".join(cities)
    print(result)

    cur.close()
    db.close()
