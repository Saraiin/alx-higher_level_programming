#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
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
    query = " ".join(["SELECT cities.name FROM cities LEFT JOIN states",
                      "ON cities.state_id = states.id",
                      "WHERE states.name = %(name)s",
                      "ORDER BY cities.id"])

     cursor = db.cursor()
    query = " ".join(["SELECT c.name FROM cities c, states st",
                      "WHERE c.state_id = st.id",
                      "AND st.name = %(name)s",
                      "ORDER BY c.id"])

    cursor.execute(query, {'name': state_name})
    rows = cursor.fetchall()
    if rows:
        list_len = len(rows)
        for i in range(list_len):
            if i != list_len - 1:
                print(rows[i][0], end=", ")
        print(rows[list_len - 1][0])
    else:
        print()

    cursor.close()
    db.close()
