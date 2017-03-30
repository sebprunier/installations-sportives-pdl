import csv

from importers.activities.ActivityLine import ActivityLine
from importers.activities.ActivityLineParser import parseRow
from importers.activities.ActivityCreator import insertActivity

def importActivities(filename):
	importedActivities = []

	with open(filename, 'rt') as csvfile:
		activitiesReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in activitiesReader:
			try:
				activityLine = parseRow(row)
				if activityLine.code not in importedActivities:
					insertActivity(activityLine)
					importedActivities.append(activityLine.code)
					# print(activityLine)
			except ValueError:
				print("Problem with row {} : {}".format(activitiesReader.line_num, ','.join(row)))

	csvfile.close()
