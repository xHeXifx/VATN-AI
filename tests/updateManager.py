from classHandling import scene, aircraft
import random
import asyncio

CS_STARTS = ["EZY", "BAW", "RYN", "TOM"] # random callsign starts

mainScene = scene()

def updateCheck(ac):
    print(f"update check called: {ac}")
    if ac.done == True:
        print(f"Aircraft {ac.callsign} is marked done. Removing...")
        mainScene.aircrafts.remove(ac)
    return

def createAircraft(): # for this test we assume the scene is 100x100 in size
    callsign = f"{random.choice(CS_STARTS)}{random.randint(100,999)}"
    while callsign in mainScene.activeCS:
        callsign = f"{random.choice(CS_STARTS)}{random.randint(100,999)}"

    if random.choice([1, 2]) == 1: # on ground
        ac = aircraft(mainScene, callsign)
    else:
        ac = aircraft(mainScene, callsign)
    ac.onUpdate.subscribe(updateCheck)
    mainScene.addAircraftToScene(ac)

async def mainLoop():
    while True:
        await asyncio.sleep(2)
        mainScene.updateAll()
    
        


createAircraft()
createAircraft()
asyncio.run(mainLoop())
