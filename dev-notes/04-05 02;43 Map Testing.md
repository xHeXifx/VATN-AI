First note and commit in a while now, ready to get back working on this

# Map Testing
We have made a mapData.json file in tests/data, this wont be the exact map used but its a okay for now as its just testing. 

# JSON Schema
Here is the schema of our map data.

### map
Declares the height and width of the map itself for building the grid

### waypoints
Each waypoint is declared here, each waypoint is a dict containing an x and y coordinate

### routes
Here is our pre-defined routes the planes themself will follow. A plane is given a route from starting, this gives them a route to follow with the waypoints object. We can then match these waypoints to the ones defined before giving an actual coordinate.

### spawns
Finally spawns, this declares where planes can spawn on the map, these are routes and the plane will start from the first coordinate on that route.


# Considirations
Just realised we dont store a z value for coords, we store x, y and yaw. Will implement z.  
Chances are each aircraft will now have a "route" variable along with this we will have a "currentWaypoint" variable. Then to determine where the aircraft will go next we will see what route they're following and the current waypoint, from this we can find the next waypoint they must be at

# 04:09
Okay got some amazing work done today and might continue further. Experimated with pygame but honestly not the biggest fan. Thinking of resorting to a web UI via flask. This might break a lot but honestly not sure what else to do

# 04:28
Tried flask but im not the best at frontend and have no idea where to even start. Honestly completely unsure on how im going to display the AC at the moment but just hoping something comes to mind. 

# Summary
NOTE: A lot of testing files broke due to this change, the changes in classHandling mean most the tests now pass too many arguments to the aircraft class.  

Okay so today did MapTraverseTest and had a sample mapdata file for waypoints, routes, etc. This now works completly it just has not the best data for now. I'll add more data when i have a good working UI.  
Pretty much re-wrote the entire classHandler, turns out the addition of mapData means we dont really need to pass anything to aircraft class as it can all be pre-determined and chose by the mapData.  
Final thing i need to do is find SOME way of showing this info, we have it all (or at least enough for testing rn) but just no way of displaying it.