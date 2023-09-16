#!/usr/bin/python3
"""script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument in a safe way
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %(name)s ORDER BY states.id"
    cur.execute(query, {'name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
