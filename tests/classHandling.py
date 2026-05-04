import json
import os
import random
# testing classes for stuff

def loadMapData():
    dataPath = os.path.join(os.path.dirname(__file__), "data", "mapData.json")
    with open(dataPath, 'r') as f:
        mapData = json.load(f)
    return mapData

class aircraft:
    def __init__(self, MainScene: scene, callsign: str): # Potential phases: [taxitorwy, holding, takeoff, climb, approach, final, taxitogate, parked]
        self.callsign = callsign
        occupiedPositions = MainScene.allACPos()

        mapData = loadMapData()

        spawn = random.choice(mapData['spawns'])

        # if what the ACs current position WILL be in occupied | This stops 2 ac from spawning ontop eachother
        while mapData['routes'][spawn['route']]['waypoints'][0] in occupiedPositions:
            spawn = random.choice(mapData['spawns'])
        
        self.routeName = spawn['route']
        self.routeData = mapData['routes'][self.routeName]
        self.currentWaypoint = self.routeData["waypoints"][0]
        self.currentWaypointIndex = 0
        
        self.posx = mapData['waypoints'][self.currentWaypoint]['x']
        self.posz = mapData['waypoints'][self.currentWaypoint]['z']
        self.altitude = spawn['altitude']
        
        self.done = False
        self.onUpdate = Event()

    def __repr__(self): # found out this lets you print the object without it saying like <classhandling.object>, pretty cool
        return (
            f"Aircraft({self.callsign}) | "
            f"pos=({self.posx},{self.posz}) | "
            f"altitude={self.altitude} | "
            f"route={self.routeName} | "
            f"wp={self.currentWaypoint} "
            f"({self.routeData['waypoints'].index(self.currentWaypoint)+1}/"
            f"{len(self.routeData['waypoints'])}) | "
            f"done={self.done}"
        )
    

    def update(self): 
        mapData = loadMapData()
        if self.done == True: # fallback. updateAll doesnt call ac with done true
            return
        
        if self.currentWaypointIndex < len(self.routeData['waypoints']) - 1:
            self.currentWaypointIndex += 1
            self.currentWaypoint = self.routeData['waypoints'][self.currentWaypointIndex]
        else:
            self.stop()

        nextWp = self.routeData['waypoints'][self.currentWaypointIndex]
        nextPosX = mapData['waypoints'][nextWp]['x']
        nextPosZ = mapData['waypoints'][nextWp]['z']

        self.posx = nextPosX
        self.posz = nextPosZ

        self.onUpdate.emit(self) # trigger event each time aircraft changes

    # NOTE: This goes for both update and stop, we need a form of TICK SYSTEM which pings everything every second or so checking for updates. this then means we can remove if
    # done is true

    def stop(self):
        self.done = True
        self.onUpdate.emit(self)
        

    # callai function in here imported from somewhere else? we could easily pass everything into it then i guess??
    # im losing track of how i want this project to go.. 



class scene: # may be temp unsure yet
    def __init__(self, groundedNum: int, inAirNum: int, aircraftObj: list[aircraft], activeCallsigns: list[str]):
        self.grounded = groundedNum
        self.inAir = inAirNum
        self.aircrafts = aircraftObj
        self.activeCS = activeCallsigns

    def __repr__(self):
        return f"Grounded: {self.grounded} | In Air: {self.inAir} | Total Aircraft: {len(self.aircrafts)} | Active Callsigns: {self.activeCS}"
    
    def addAircraftToScene(self, aircraftObj: aircraft):
        self.aircrafts.append(aircraftObj)
        
        if aircraftObj.altitude == 0:
            self.grounded = self.grounded + 1
        else:
            self.inAir = self.inAir + 1

        self.activeCS.append(aircraftObj.callsign)
    
    def updateAll(self, debug=False): # temp while we have no perminant aircraft route
        for ac in self.aircrafts:
            if ac.done != True:
                ac.update()
                if debug == True: print(ac)
            else:
                self.aircrafts.remove(ac)

    def allACPos(self):
        positions = []
        for ac in self.aircrafts:
            positions.append(ac.currentWaypoint)
        return positions

class Event: # gonna try get a tick system functioning in this
    def __init__(self):
        self._subscribers = []

    def subscribe(self, func):
        self._subscribers.append(func)

    def emit(self, *args, **kwargs):
        for func in self._subscribers:
            func(*args, **kwargs)
         