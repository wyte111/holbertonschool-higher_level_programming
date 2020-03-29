#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
        host="localhost", user=argv[1],
        passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id LIMIT 5")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
    cur.close()