import json
import os
# This file will contain general tests for random stuff
# i will try keep every test i do in here in functions

def TEST_aircraftRemovingAndExternalCreation(): # Testing creation of objects outside the class handling file and a mock tick system kinda?
    from classHandling import aircraft, scene
    mainScene = scene()

    aircrafts = []

    test123 = aircraft(mainScene, "ezy123")
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
    from classHandling import aircraft, scene
    mainScene = scene()

    aircrafts = []
    test = aircraft(mainScene, "ezy123")
    test1 = aircraft(mainScene, "ezy124")
    test2 = aircraft(mainScene, "ezy125")
    aircrafts.append(test)
    aircrafts.append(test1)
    aircrafts.append(test2)

    for craft in aircrafts:
        print(craft)

def TEST_sceneClassWithAircraft():
    from classHandling import aircraft, scene
    mainScene = scene()
    test = aircraft(mainScene, "ezy123")
    test2 = aircraft(mainScene, "ezy123")

    mainScene.addAircraftToScene(test)
    mainScene.addAircraftToScene(test2)

    print(mainScene)
    
def TEST_tickUpdateEventSystem():
    from classHandling import aircraft, scene
    mainScene = scene()

    def printAlt(ac):
        print(f"ALT: {ac.altitude}")

    a = aircraft(mainScene, "ezy123")

    a.onUpdate.subscribe(printAlt)

    a.update()

def TEST_noVarAircraft():
    # just a simple test seeing if objects can be differenciated with no variable names in an array
    from classHandling import aircraft, scene
    mainScene = scene()
    aircrafts = []
    
    aircrafts.append(aircraft(mainScene, "ezy123"))
    aircrafts.append(aircraft(mainScene, "ezy124"))
    aircrafts.append(aircraft(mainScene, "ezy125"))

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
    
def TEST_newAircraftClass():
    # all other aircrafts are now broken as theyre missing parameters
    from classHandling import aircraft, scene
    mainScene = scene()
    dataPath = os.path.join(os.path.dirname(__file__), "data", "mapData.json")
    with open(dataPath, 'r') as f:
        data = json.load(f)
    
    routeData = data['routes']['arrival_west']

    testAircraft = aircraft(mainScene, "ezy123")
    print(testAircraft) # callsign: ezy123 | posx: 0 | posz: 0 | posy: 0 | yaw: 0 | altitude: 0 | routeName: arrival_west | currentWaypoint: W1 |done: False



TEST_newAircraftClass()