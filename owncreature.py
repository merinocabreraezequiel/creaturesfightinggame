#imports
import json

creature = ""

def loadYourCreature():
    global creature
    f = open("owncreature.json", "r")
    string_own_creature_double_quotes = f.read()
    creature = json.loads(string_own_creature_double_quotes)
    print('own_creature: '+str(creature["creature"]["name"]))

def updateYourCreature():
    global creature
    with open('owncreature.json', 'w') as outfile:
        json.dump(creature, outfile)

def getEngery():
    global creature
    print ("get Engery: "+str(creature["creature"]["energy"]))
    return creature["creature"]["energy"]
    
def setEngery(newEnergy):
    global creature
    creature["creature"]["energy"] = newEnergy
    print ("set Engery: "+str(creature["creature"]["energy"]))