#!/usr/bin/python3
"""
script that takes in an argument
and displays all values in the states table
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    MySQL Connection
    """
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    states = cur.fetchall()
    [print(state) for state in states]
