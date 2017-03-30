import sqlite3

from services.activities.Activity import Activity

def allActivities():
    activities = []

    conn = sqlite3.connect('installations.db')
    c = conn.cursor()

    c.execute("SELECT code, label FROM activities")
    for row in c:
        activities.append(Activity(row[0], row[1]))
        # print(row)

    conn.close()

    return activities
