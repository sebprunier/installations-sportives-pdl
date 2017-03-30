import sqlite3

from importers.activities.ActivityLine import ActivityLine

def insertActivity(activity):
    conn = sqlite3.connect('installations.db')
    c = conn.cursor()
    insertQuery = "INSERT INTO activities(code, label) VALUES (?, ?)"
    c.execute(insertQuery, (activity.code, activity.label))
    conn.commit()
    conn.close()
