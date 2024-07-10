#!/usr/bin/python3
""" Lists all rows in table states from database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# executed when not imported
if __name__ == '__main__':

    # connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
