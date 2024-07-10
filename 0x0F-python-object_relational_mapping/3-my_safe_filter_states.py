#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Execute the query with parameterized query
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    # Fetch all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up process
    cur.close()
    db.close()
