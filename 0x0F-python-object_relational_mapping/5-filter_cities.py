#!/usr/bin/python3
"""
Takes in the name of a state as an argument and
list all cities of that state, using the database 'hbtn_0e_4_usa'
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
        "SELECT cities.name FROM cities WHERE cities.state_id = "
        "(SELECT states.id FROM states WHERE states.name = '{}')".format(name)
    )
    rows = cursor.fetchall()
    if rows:
        len_rows = len(rows)
        for i in range(len_rows):
            if i == len_rows - 1:
                print(rows[i][0])
            else:
                print(rows[i][0], end=", ")
    else:
        print()

    cursor.close()
    mydb.close()
