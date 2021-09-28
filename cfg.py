#imports
import pygame
import json
from json import JSONEncoder

import owncreature

#global vars
creature = ""
objects = ""
yourCreature = ""

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("resources\logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    FPS = 30 # frames per second setting
    fpsClock = pygame.time.Clock()
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180), 0, 32)
     
    #add image to display
    image = pygame.image.load("resources\image1.png")
    background = pygame.image.load("resources\\background.png")
    background = pygame.transform.scale(background, (240, 180))
    screen.blit(background, (0,0))
    image.set_alpha(None)
    image.set_colorkey((255,0,255))
    screen.blit(image, (50,50))
    pygame.display.flip()
    fpsClock.tick(FPS)

    # define the position of the smiley
    xpos = 50
    ypos = 50
    # how many pixels we move our smiley each frame
    step_x = 10
    step_y = 10

    # define a variable to control the main loop
    running = True
    
    #load elements
    loadCriatures()
    loadObjects()

    owncreature.loadYourCreature()

    owncreature.setEngery(owncreature.getEngery() - calculateHit(creature["creatures"][0]["properties"]["strength"],True,True))
    owncreature.setEngery(owncreature.getEngery() - calculateHit(creature["creatures"][0]["properties"]["strength"],True,False))
    owncreature.setEngery(owncreature.getEngery() - calculateHit(creature["creatures"][0]["properties"]["strength"],False,True))
    owncreature.setEngery(owncreature.getEngery() - calculateHit(creature["creatures"][0]["properties"]["strength"],False,False))

    owncreature.updateYourCreature()
    ownCreatureCaptabilities = owncreature.getCapabilities()
    print ("owncreaturecapabilities"+str(ownCreatureCaptabilities))


    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        
        # check if the smiley is still on screen, if not change direction
        if xpos>240-64 or xpos<0:
            step_x = -step_x
        if ypos>180-64 or ypos<0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x # move it to the right
        ypos += step_y # move it down
        # first erase the screen 
        screen.blit(background, (0,0))
        # now blit the smiley on screen
        screen.blit(image, (xpos, ypos))
        # and update the screen (don't forget that!)
        pygame.display.update()
        fpsClock.tick(FPS)

def loadCriatures():
    global creature
    f = open("creatures.json", "r")
    string_creatures_double_quotes = f.read()
    creature = json.loads(string_creatures_double_quotes)
    print('creature: '+str(creature["creatures"]))

def loadObjects():
    global objects
    f = open("objects.json", "r")
    string_objects_double_quotes = f.read()
    objects = json.loads(string_objects_double_quotes)
    print('objects: '+str(objects))

def JSONElementsCount(totalCountsJSON):
    return len(totalCountsJSON)
    #print(x.name, x.capabilities, x.weaknesses, x.energy)

def calculateHit(strength, attack_capability, defense_weakness):
    aws = 1.5 if attack_capability else 1
    dws = 0.75 if defense_weakness else 1
    return strength * aws * dws

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()