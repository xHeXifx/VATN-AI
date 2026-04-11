# testing classes for stuff

class aircraft:
    def __init__(self, callsign: str, posx: int, posy: int, yaw: int, altitude: int, phase: str): # Potential phases: [taxitorwy, holding, takeoff, climb, approach, final, taxitogate, parked]
        self.callsign = callsign
        self.posx = posx
        self.posy = posy
        self.yaw = yaw
        self.altitude = altitude
        self.phase = phase
        self.done = False
        self.onUpdate = Event()

    def __repr__(self): # found out this lets you print the object without it saying like <classhandling.object>, pretty cool
        return f"callsign: {self.callsign} | posx: {self.posx} | posy: {self.posy} | yaw: {self.yaw} | altitude: {self.altitude} | phase: {self.phase} | done: {self.done}"
    

    def update(self, posx: int, posy: int, yaw: int, altitude: int): # TODO: Figure out how i want the next positions to be calculated, will probs be following route but still.
        self.posx = posx
        self.posy = posy
        self.yaw = yaw
        self.altitude = altitude
        # self.phase TODO: Want to automatically calculate when a certain phase is active, this is possible when we setup a scene and frame of airport

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
    
    def updateAll(self): # temp while we have no perminant aircraft route
        for ac in self.aircrafts:
            ac.update(ac.posx + 1, ac.posy + 1, ac.yaw + 1, ac.altitude)


class Event: # gonna try get a tick system functioning in this
    def __init__(self):
        self._subscribers = []

    def subscribe(self, func):
        self._subscribers.append(func)

    def emit(self, *args, **kwargs):
        for func in self._subscribers:
            func(*args, **kwargs)
         