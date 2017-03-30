from importers.activities.ActivityImporter import importActivities
from admin.DatabaseAdmin import createActivityTable

# TODO import other data : installations, equipements

createActivityTable()
importActivities('../data/activites.csv')
