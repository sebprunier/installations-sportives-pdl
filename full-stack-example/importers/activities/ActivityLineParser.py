from importers.activities.ActivityLine import ActivityLine

def parseRow(row):
    code = int(row[4].strip())
    label = row[5].strip()
    return ActivityLine(code, label)
