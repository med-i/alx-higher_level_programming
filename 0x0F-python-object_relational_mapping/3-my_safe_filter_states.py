#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

import sys
import MySQLdb


def main():
    """
    Ensures that the script runs only when executed directly,
    not when imported as a module.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states WHERE name = %s", (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
