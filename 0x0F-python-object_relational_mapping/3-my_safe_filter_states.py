#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of 'hbtn_0e_0_usa' where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    name = sys.argv[4].split("'", maxsplit=1)[0]
    cursor = mydb.cursor()
    cursor.execute(
        ("SELECT * FROM states WHERE states.name = '{}' "
         "ORDER BY states.id ASC").format(name)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    mydb.close()
