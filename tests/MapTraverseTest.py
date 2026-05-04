# Test for mapData.json attempting to make planes follow a pre-determined route. 
# Read /tests/data/mapData.json to get an understanding of the structure
from classHandling import scene, aircraft
import random
import asyncio

CS_STARTS = ["EZY", "BAW", "RYN", "TOM"] # random callsign starts

mainScene = scene()

def updateCheck(ac):
    print(f"update check called: {ac}")
    return

def createAircraft(): # for this test we assume the scene is 100x100 in size
    callsign = f"{random.choice(CS_STARTS)}{random.randint(100,999)}"
    while callsign in mainScene.activeCS:
        callsign = f"{random.choice(CS_STARTS)}{random.randint(100,999)}"

    ac = aircraft(mainScene, callsign)

    ac.onUpdate.subscribe(updateCheck)
    mainScene.addAircraftToScene(ac)
    return ac

async def mainLoop():
    while True:
        await asyncio.sleep(2)
        mainScene.updateAll()
    
    
createAircraft()

try:
    asyncio.run(mainLoop())
except KeyboardInterrupt:
    print("Done.")
