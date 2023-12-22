#!/usr/bin/python3
"""
This script displays all values in the states
table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT DISTINCT * FROM states WHERE \
                name = %s ORDER BY id", (state_name,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
