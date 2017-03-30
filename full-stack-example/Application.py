from libs.bottle import route, static_file, run
import json

from services.activities.ActivityService import allActivities

@route('/api/activities')
def activities():
    activities = allActivities()
    jsonActivities = []
    for activity in activities:
        jsonActivities.append(activity.__dict__)
    return { "activities" : jsonActivities }

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')

run(host='localhost', port=8888)
