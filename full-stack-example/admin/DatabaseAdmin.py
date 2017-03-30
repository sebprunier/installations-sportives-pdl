import sqlite3

def createActivityTable():
    conn = sqlite3.connect('installations.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS activities")
    c.execute('''CREATE TABLE activities
                 (code integer PRIMARY KEY, label text)''')
    conn.commit()
    conn.close()
