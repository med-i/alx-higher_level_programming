#!/usr/bin/python3
"""
This module
"""

import sys
import MySQLdb


def main():
    """Main"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
