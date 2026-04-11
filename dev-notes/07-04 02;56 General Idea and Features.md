## Idea
So heres my idea, we create a python program that lets you work as a ATC controller, thats pretty much it..

## Feature ideas / How stuff will work (hopefully)
- So i intend to use this on my Silicon Mac, integrating AI into this would be lovely but costly and we dont want that. I recently learnt of the program "apfel" which lets you use the Apple intelligence LLM stored locally for your own use, this would be good to use.
- METAR/ATIS: Start with a artifical start date so we can control days (will probs be 1/1/2026) then use estimated season and weather times (somehow) to decide elements like temperature, wind speed throughout the day, weather events, etc.
- Frequencies: Recieve all frequencies at once but show something like [TO GROUND] {text} or TOWER, CONTROL, etc. Maybe choose to just do one at a time though unsure. 
- GUI: I wanna use something like the VATSIM controller gui as this looks great and is pretty much exactly what im looking for, this will be a challenege however. Would simplify a lot however. The refference image i'll most likely use is [here](https://i.ytimg.com/vi/kqwNzP7otpg/maxresdefault.jpg).

- Basic logic framework: Okay so this whole project is gonna be a LOT of moving parts at once for this we will defo need to use async, this is something i havent entirely wrapped my head around so im gonna need to research this a little before i start. I would like to contain everything in seperate files for ease of use so like weather, traffic, data storage, etc just to keep everything somewhat organised.


## Further Notes:
- As AI has grown i've found myself relying on it more often, like if i forget syntax i go to AI for help instead of finding the problem myself; I would like to break out of this which is another big reason for this project i wanna do something that i feel i could do without the immediate help of AI and relying on stuff like stackoverflow and docs like the good ol days 😭 The one thing im allowing AI for here is the ATCs system prompt as im not great at typing those out while ensuring a good response.

## Expansion:
- TTS and STT: I would LOVE to implement TTS at some point, makes it just feel a lot better. STT should be fairly easy with openai-whisper but i have had some issues with it before so unsure at that. TTS on the other hand i KNOW is gonna be so annoying, the amount of good sounding TTS modules out there is scarse or paid/online and i do not want this. Further on TTS, i wanna apply a radio effect to the responses and yet again unsure of how to do that.

### [Back](/dev-notes.md)