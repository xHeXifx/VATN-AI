# This file will contain general tests for random stuff
# i will try keep every test i do in here in functions

def TEST_aircraftRemovingAndExternalCreation(): # Testing creation of objects outside the class handling file and a mock tick system kinda?
    from classHandling import aircraft

    aircrafts = []

    test123 = aircraft("ezy123", 1, 2, 3, 0, "landing")
    aircrafts.append(test123)

    for i in range(5):
        print(i)
        if i == 4:
            test123.stop()
        for craft in aircrafts:
            if craft.done == True:
                aircrafts.remove(craft)
                print("Aircraft stopped")
            else:
                print("not done")

def TEST_aircraftDetailsList(): # Testing how we can get all details on a aircraft, we cant really but we can do __repr__ in the class handling which we added
    from classHandling import aircraft

    aircrafts = []
    test = aircraft("ezy123", 1, 2, 3, 1000, "landing")
    test1 = aircraft("ezy124", 1, 2, 3, 900, "landing")
    test2 = aircraft("ezy125", 1, 2, 3, 500, "landing")
    aircrafts.append(test)
    aircrafts.append(test1)
    aircrafts.append(test2)

    for craft in aircrafts:
        print(craft)

def TEST_sceneClassWithAircraft():
    from classHandling import aircraft, scene
    mainScene = scene(0, 0, [], [])
    test = aircraft("ezy123", 1, 2, 3, 200, "takeoff")
    test2 = aircraft("ezy123", 1, 2, 3, 0, "taxitorwy")

    mainScene.addAircraftToScene(test)
    mainScene.addAircraftToScene(test2)

    print(mainScene)
    
def TEST_tickUpdateEventSystem():
    from classHandling import aircraft

    def printAlt(ac):
        print(f"ALT: {ac.altitude}")

    a = aircraft("ezy123", 1, 2, 3, 0, "parked")

    a.onUpdate.subscribe(printAlt)

    a.update(2, 3, 4, 100)

def TEST_noVarAircraft():
    # just a simple test seeing if objects can be differenciated with no variable names in an array
    from classHandling import aircraft
    aircrafts = []
    
    aircrafts.append(aircraft("ezy123", 1, 2, 3, 1000, "landing"))
    aircrafts.append(aircraft("ezy124", 1, 2, 3, 900, "landing"))
    aircrafts.append(aircraft("ezy125", 1, 2, 3, 500, "landing"))

    for ac in aircrafts: # turns out this is a good way to find a specific non-var object, didnt think looping through would be efficient
        if ac.callsign == "ezy125":
            print()
            # return ac
    # return None

    # update non-var aircraft in array

    for ac in aircrafts:
        if ac.callsign == "ezy124":
            ac.update(2, 3, 4, 0)
            break
    

TEST_sceneClassWithAircraft()