# Depreacted prob
# Rlly stuck on how im going to display. Read devnote 04-05

from flask import Flask, render_template, jsonify
import json
from classHandling import scene, aircraft, loadMapData
import random

CS_STARTS = ["EZY", "BAW", "RYN", "TOM"]

app = Flask(__name__)
mapData = loadMapData()

mainScene = scene(0, 0, [], [])
mainScene.addAircraftToScene(aircraft(mainScene, f"{random.choice(CS_STARTS)}{random.randint(100,999)}"))
mainScene.addAircraftToScene(aircraft(mainScene, f"{random.choice(CS_STARTS)}{random.randint(100,999)}"))
mainScene.addAircraftToScene(aircraft(mainScene, f"{random.choice(CS_STARTS)}{random.randint(100,999)}"))

@app.route('/')
def renderIndex():
    return render_template('index.html')

@app.route('/api/getMainScene')
def getMainScene():
    data = {}
    data['repr'] = str(mainScene)
    data['grounded'] = mainScene.grounded
    data['in-air'] = mainScene.inAir
    data['activeCS'] = mainScene.activeCS
    data['aircraft'] = []

    for ac in mainScene.aircrafts:
        data['aircraft'].append({
            "callsign": ac.callsign,
            "posx": ac.posx,
            "posz": ac.posz,
            "altitude": ac.altitude,
            "waypoint": ac.currentWaypoint,
            "waypointIndex": ac.currentWaypointIndex,
            "routeData": ac.routeData,
            "routeName": ac.routeName,
            "done": ac.done
        })

    return jsonify(data)

@app.route('/api/updateAll')
def updateAllAC():
    try:
        mainScene.updateAll()
        return {"status": "ok"}
    except Exception as e:
        return {"status": e}

    

app.run(debug=True)