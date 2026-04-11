# testing classes for stuff

class aircraft:
    def __init__(self, callsign: str, posx: int, posy: int, yaw: int, phase: str): # Potential phases: [taxitorwy, holding, takeoff, climb, approach, final, taxitogate, parked]
        self.callsign = callsign
        self.posx = posx
        self.posy = posy
        self.yaw = yaw
        self.phase = phase
        self.done = False

    def update(self, posx, posy, yaw): # TODO: Figure out how i want the next positions to be calculated, will probs be following route but still.
        self.posx = posx
        self.posy = posy
        self.yaw = yaw
    # NOTE: This goes for both update and stop, we need a form of tick system which pings everything every second or so checking for updates. this then means we can remove if
    # done is true

    def stop(self):
        self.done = True
            

    # callai function in here imported from somewhere else? we could easily pass everything into it then i guess??
    # im losing track of how i want this project to go.. 

