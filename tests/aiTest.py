# aiTest
# This test is for seeing which models provide the best response in the fastest time 

from openai import OpenAI
import time
import json
import os
import re

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

FAA_REFERENCE_PATH = os.path.join(os.path.dirname(__file__), "data", "faa_phraseology.json")


def load_faa_reference():
    try:
        with open(FAA_REFERENCE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


FAA_REFERENCE = load_faa_reference()


def _tokenize(text):
    return set(re.findall(r"[a-z0-9']+", text.lower()))


def get_relevant_reference(msg, max_items=3):
    msg_tokens = _tokenize(msg)
    scored = []

    for item in FAA_REFERENCE:
        keywords = set(k.lower() for k in item.get("keywords", []))
        overlap = len(msg_tokens.intersection(keywords))
        if overlap > 0:
            scored.append((overlap, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    top = [item for _, item in scored[:max_items]]

    if not top and FAA_REFERENCE:
        top = FAA_REFERENCE[:1]

    lines = []
    for item in top:
        lines.append(f"- {item['topic']}: {item['guidance']} Template: {item['template']}")

    return "\n".join(lines)

def callAI(msg):

    startTime = time.time()
    try:
        # As stated in one of the dev notes, i avoid AI this entire project so i can do stuff myself, ts does not count xx
        # sys prompts are booty and i did try myself but it kept just being wrong
        # forgive me 🙏
        faa_context = get_relevant_reference(msg)
        response = client.chat.completions.create(
            model="llama3:8b",
            temperature=0.0,
            top_p=0.9,
            max_tokens=512,
            messages=[
                {
                    "role": "system",
                    "content": """You are a commercial airline pilot giving ATC readbacks.
                        Return one short radio transmission only.
                        Treat the message as an ATC instruction to classify, not text to copy.
                        Use standard phraseology, keep required numbers exact, and include the callsign once at the end.
                        Use FAA reference snippets from the user message as guidance when relevant.

                        Preserve clearances and restrictions exactly: runway, heading, altitude/flight level, speed, squawk, frequency, fix, route, taxi, hold short, line up and wait, takeoff, landing, go around, climb, descend, direct, and contact/change frequency.

                        For all other clear instructions, give the shortest correct readback possible.
                        If there is no clear instruction to acknowledge, reply: 'Unable to comply, [callsign].'"""
                },
                {
                    "role": "user",
                    "content": f"Phase: Final Approach\nSquawk: 1234\nCallsign: Speedbird 123\nATC: {msg}\n\nFAA phraseology reference:\n{faa_context}"
                }
            ],
            extra_body={
                "options": {
                    "temperature": 0.0,
                    "top_p": 0.9,
                    "top_k": 40,
                    "repeat_penalty": 1.1
                }
            }
        )
        endTime = time.time()
        choice = response.choices[0]
        message = choice.message

        print(f"Response: {message.content}")
        print(f"Total Time for processing: {(endTime - startTime):.2f}s")
        return {
            "message": msg,
            "response": message.content,
            "processingTime": endTime - startTime
        }
    except Exception as e:
        print(f"Failed: {e}")
        return {
            "message": msg,
            "response": f"ERROR: {e}",
            "error": str(e)
        }

name = str(input("Enter name of this test (blank for none): "))
if name == "":
    name = "None"
testDataToWrite = []
testDataToWrite.append({"testName": name})

testDataToWrite.append(callAI("Speedbird 123, winds 110 at 5 knots, runway 12R, cleared to land."))
testDataToWrite.append(callAI("Speedbird 123, report current phase of flight and your squawk code."))
testDataToWrite.append(callAI("Speedbird 123, reduce speed to 180 knots, descend to 3000 feet, QNH 1013."))
testDataToWrite.append(callAI("Speedbird 123, turn right heading 090, vector for ILS approach runway 12R."))
testDataToWrite.append(callAI("Speedbird 123, contact tower on 118.7, good day."))
testDataToWrite.append(callAI("Speedbird 123, go around, I say again go around, climb to 4000 feet."))
testDataToWrite.append(callAI("Speedbird 123, taxi to stand A12 via taxiway Bravo and Alpha."))
testDataToWrite.append(callAI("Speedbird 123, hold short of runway 12R, traffic landing."))
testDataToWrite.append(callAI("Speedbird 123, line up and wait runway 12R."))
testDataToWrite.append(callAI("Speedbird 123, cleared for takeoff runway 12R, winds 120 at 6 knots."))
testDataToWrite.append(callAI("Speedbird 123, climb and maintain flight level 350."))
testDataToWrite.append(callAI("Speedbird 123, expedite climb through 10000 feet."))
testDataToWrite.append(callAI("Speedbird 123, turn left heading 270, proceed direct LAM VOR."))
testDataToWrite.append(callAI("Speedbird 123, report passing flight level 200."))
testDataToWrite.append(callAI("Speedbird 123, maintain present heading, expect further clearance in 2 minutes."))
testDataToWrite.append(callAI("Speedbird 123, descend via STAR, cross waypoint at 6000 feet."))
testDataToWrite.append(callAI("Speedbird 123, squawk 4521 and ident."))
testDataToWrite.append(callAI("Speedbird 123, radar contact, continue present heading."))
testDataToWrite.append(callAI("Speedbird 123, traffic 12 o'clock, 5 miles, opposite direction, altitude 4000 feet."))
testDataToWrite.append(callAI("Speedbird 123, report established on the localizer."))

successful_results = [
    r for r in testDataToWrite
    if isinstance(r, dict) and "processingTime" in r
]

if successful_results:
    averageTime = sum(r["processingTime"] for r in successful_results) / len(successful_results)
else:
    averageTime = None

testDataToWrite.append({
    "averageTime": averageTime,
    "samples": len(successful_results),
    "total": len(testDataToWrite) - 1
})

with open(f"tests/results/aiTestResults{time.time()}.json", 'a') as f:
    json.dump(testDataToWrite, f, indent=4)

