#!/usr/bin/python3
""" This script lists all states fwith a name starting
with N (upper N)rom the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE \
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
