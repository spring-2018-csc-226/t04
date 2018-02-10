######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T04: Adventure in Gitland
#
# Purpose: To recreate a choose-your-own-adventure style game
# by refactoring T01.
#
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
#
# This new version will take advantage of functions, as well as
# demonstrate the value of git as a tool for collaborating.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

import random
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False


def intro():
    """
    Introduction text for the story. Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(delay)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(delay * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(delay)
    return user


def end_story(user):
    """
    This is the ending to the story. Don't modify this function, either.

    :param user: the user's name

    :return: None
    """
    print("Congratulations, " + user + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay*5)
    print("Now go away.")


def team_1_adv():
    global dead
    direction=input("Which way you gon go? [East/West]\n")
    if direction == "East":
        # Bravo!
        print("You are in front of Building 1 and Building 2, both are gigantic and luxurious.")
    building = input("Which building would you pick? [Building 1/Building 2] \n")
    if building == "Building 1":
        # Smart Choice
        print("Seems someone has a surprise for you...")
        print("WOW! Welcome to the wonderland where you will be presented a 32 carat diamond Worth $150,000.")
        dead = False
    else: # elif building == "Building 2":
        # Bad Choice
        print("Welcome to the dragon's home where no one ever survives.")
        print("You are trying to escape, but the door behind you is already shut, you have no option but wait on the dragon.")
        dead = True
    are_you_dead(dead)


def team_2_adv():
    pass
    # TODO Add your code here


def team_3_adv():
    pass
    # # https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-cohen
    # Team 3
    """
    Asks for a response then prints the corresponding output. 
    
    Asks for amount of days and prints another corresponding output.
    """
    t3_question_1()
    are_you_dead(dead)
    t3_question_2()
    are_you_dead(dead)

def t3_question_1():
    global dead
    print('The true love of your life awaits at the bottom of the stairs.')
    print('Time is short, and you must whisper something in his/her ear.')
    while 1:
        response = input("How does s/he respond? [cry / embrace / laugh]")
        if response == "cry":
            print("Your resolve weakens and you find yourself unable to kill him.")
            print("You sign the document, and your fate is sealed.")
            dead = True
            break
        elif response == "embrace":
            print("You stab him in the thigh, and vengeance is yours! You step over his gory body and walk out of the house...")
            sleep(delay)
            break
        elif response == "laugh":
            print("You discover to your chagrin that you cannot enact your plan immediately."
                  "You turn and use the knife on the parsnips and yams. How disappointing, but the romance continues...")
            sleep(delay)
            break
        else:
            print("You have chosen a destiny that is beyond the boundaries of the mind.")
            print("You are incomprehensible. You stare blankly ahead.")
            print("The true love of your life awaits at the bottom of the stairs.")
            print("Time is short, and you must whisper something in his/her ear.")


def t3_question_2():
    global dead
    print("After weeping your harbor of salty tears and feeling them dry on your cracked cheeks,")
    print("John Waters style, you decide to bide your time before your next attempt.")
    days = int(input("How long do you wait? [length in days]"))
    if days < 2:
        print("In your rush to get out of this terrible, horrible, no good situation, you let your plan be discovered. Oops.")
        dead = True
    elif days >= 7:
        print("You conniving, meretricious, deceptive, dissembling, disingenious, duplicitous shark!")
        print("You win. Muhuhahahah. On to your next victim.")
        sleep(delay)
    else:
        print("You are just not quite sure yet about how to proceed. Better keep on truckin'.")
        sleep(delay)


########################################################################################################################
def team_4_adv():
    # https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-berucha-susan
    # Team 4
    print()
    global dead
    sleep(delay)
    print("You now have three doors in front of you. The first door says, 'ULTIMATE DEATH'. The second door says, 'FREEDOM'. The last door say, 'HAPPINESS AWAITS'.")
    door = input("Which door do you dare pick? [First/Second/Third]")
    sleep(delay)

    print()
    if door == "First":
        # Good Choice!
        print("Hahaha, you Daredevil!")
        print("You cannot be fooled.. or were you ready for this story to be over?")
        print("Either way, you have found your way to FREEDOM!")
        sleep(delay)
        print()
    elif door == "Second":
        # Ohhh, better luck next time!
        print("Ahhhh...")
        print("Did I say 'Freedom'??")
        print("I meant DEATH!!!")
        print("You enter through the door and fall into lava.")
        print("Look on the bright side, at least you died quickly!")
        dead = True
        sleep(delay)
        print()
    else:
        # Neutral choice
        print("You enter through the door and you are in a land of puppies and kitties! Lucky you!")
        print("Told you happiness awaits!")
        print("However, the door disappears behind you and now you have to still find your way out to freedom.")
        print("Hope you don't have allergies!")
    sleep(delay)

    if dead:
        quit()
        print("Good luck on your next adventure!")




def team_5_adv():
     # TODO Add your code here
    # The next chapter
    dead = False
    direction = input("Which direction would you like to go now? [North/South/East/West]")

    if direction == "West":
        # Good choice.
        print("You have found food. Now you might not starve to death. Congratulations.")
        sleep(delay)
    elif direction == "North":
        # Bad choice.
        print("Suddenly you hear a rumbling above you. You look up to see a falling bolder.")
        sleep(delay)
        number = int(input("Choose a number to determine your fate. [1-10]"))
        if number >= 6:
            # Good choice.
            print("You see the bolder just in time and dodge out of the way.")
            print("You are still alive good for you!")
        else:
            print("...")
            print("You have been crushed by a boulder.")
            dead = True
    else:
        # Neutral choice.
        print("You keep walking until you hit a dead end.")
        sleep(delay)

    if dead == True:
        quit()


def team_6_adv():
    #######################################################################################################
    # https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-annette-and-azah
    # Team 6 Robert Kaleb
    global dead
    print("Hurray! You see a light in the distance! Because you are so light deprived, you immediately go towards it and find the side a mountain.")
    print("Now you have to decide which way to go.")
    direction = input("Do you want to climb [Up/Down/Left/Right]")

    if direction == "Up":
        # Would be a good choice... too bad it's raining!
        print("You start to climb up, but since it is raining, the rocks are wet and slippery. You lose your grip and fall to your death.")
        sleep(delay)
        dead = True
    elif direction == "Down":
        # Better choice!
        print("You start to climb down and realize you're only a few feet from the ground.")
        print("Unfortunately for you, you step into a nest of vicious fairies. In their anger, they carry you away to Fairy Land.")
        sleep(delay)
        dead = False
    elif direction == "Left":
        # Hope you're not too afraid of spiders...
        print("You decided to go to the left, where a narrow rock ledge leads around the corner.")
        print("You follow the ledge, and discover a staircase going up the mountain.")
        print("Your curiosity overcomes you, and you decide to climb up the staircase.")
        sleep(delay)
        dead = False
    elif direction == "Right":
        # So sad to die so close to the ground.
        print("You turn right at the entrance to the cave and see a ledge leading around the corner of the mountain.")
        print("You walk along the ledge, but soon realize that the rocks are unstable.")
        print("Oh no! The rocks begin to tumble out from under you feet. An avalanche begins and rocks start tumbling around you.")
        sleep(delay)
        print("You have a few seconds to decide what to do.")
        print("You see a ledge just above your head and decide to jump for it!")
        height = int(input("How many feet away is the ledge?"))
        if height < 5:
            print("Oops, you didn't reach far enough! You fall into the avalanche and die.")
            dead = True
        elif height > 5:
            print("Good guess! You gauged the correct distance and are dangling on the ledge, holding on for dear life as the avalanche falls around you.")
            dead = False
        else:
            print("Well, that didn't work.")
            dead = True
    else:
        # Neutral choice
        print("Paralyzed by indecision, you said in the opening of the tunnel, looking out.")
        sleep(delay)
        print("The sun sets on your hopes and dream.")
        dead = False

    # TODO Don't forget to check if your user is dead at the end of your chapter!

    if dead:
        quit()
    ###############################################################################################
        pass
        # TODO Add your code here


def team_7_adv():
    pass
    # TODO Add your code here


def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():
    def choice_1():
        print("It's a trap! You were forced to attend Berea College for 4 years, get a decent job, and died at the age of 102.")
        dead = True
    def choice_2():
        print("You sit in the chair and you wake up 3 hours later, you just wasted 3 hours")
    def choice_3():
        print("As you walk away, you find some sneakers with +5 jump on your path.")
        sleep(delay*2)
        print("You try to jump with your new +5 sneakers, you jump and quickly find yourself free from the gravity, your journey should go mush quicker now.")




    def main_9(): # Our main function for our chapter to help us organize.
        print("")
        print("You see a chair to you left, 'odd place for a chair,' you think.")
        sleep(delay*2)
        print("")
        print("To your right you see a Berea College official hat signed by President Lyle Roelofs, worth $34.29 on eBay")
        sleep(delay*3)
        choice = input("Do you sit in the chair, or pick up the hat? [Pick up hat/Sit in chair/Walk away]")
        choice = choice.lower()
        while choice != "pick up hat" and choice != "sit in chair" and choice != "walk away":
            choice = input("Do you sit in the chair, or pick up the hat? [Pick up hat/Sit in chair/walk away]")
            choice = choice.lower()



            # Different choice outcomes are defined as functions.
        if choice == "pick up hat":
            choice_1()
        elif choice == "sit in chair":
            choice_2()
        elif choice == "walk away":
            choice_3()
        if dead ==True:
            quit()
    main_9()
    # TODO Add your code here


def team_10_adv():
    global dead

    print("You encounter a set of two doors, which door do you take? [Door 1/Door 2]")
    direction = input()
    
    if direction == "Door 1":
        print("You have selected Door 1.")
        print("There is a path that leads you further in your quest.")
    elif direction == "Door 2":
        print("You have selected Door 2.")
        print("Oh no! There's a man-eating goat!")
        print("If you can guess his favorite number, then he will not eat you.")
        num_guess = int(input("What do you think it is?"))
        if num_guess > 8 or num_guess < 8:
            print("The goat is impressed with your knowledge of astrology, a skill that totally has an actual purpose.")
            print("He tells you the path lies behind Door 1, and you continue on your quest.")
        elif num_guess == 8:
            print("The goat is angered by your audacity at such an invalid attempt. I'm sorry, but he has eaten you.")
            dead = True
        else:
            print("The goat is angered by your ignorance. I'm sorry, but he has eaten you.")
            dead = True
        if dead:
            quit()
        # TODO Add your code here


def team_11_adv():
    pass
    # TODO Add your code here


def team_12_adv():
    pass
    # TODO Add your code here


def team_13_adv():
    pass
    # TODO Add your code here


def team_14_adv():
    global dead
    print("You've come to across two separate tunnels.")
    print()
    direction = input("Which way do you go? (Left/Right/Go Back)")
    if direction == "Left":
        #Bad choice
        print("OH NO! The cave collapsed behind you. You'll survive for two more days before dying from lack of oxygen.")
        dead = True

    elif direction == "Right":
        #Good choice
        print("You found a sandwich, gained 10 HP.")

    elif direction == "Go Back":
        #Neutral choice
        print("You chickened out! You're still stuck wandering the cave.")

    else:
        print("You find a wall with a combination lock on it.")
        die = int (input("Please enter a number 0-100"))
        if die >= 50:
            print("You enter the wrong combination and the walls close in around you.")
            dead = True
        elif die <= 49:
            print("The door opens and you continue deeper into the cave.")
    # TODO Don't forget to check if your user is dead at the end of your chapter!
    if dead == True:
        print("You died")
        quit()


def team_15_adv():
    pass
    # TODO Add your code here


def team_16_adv():
    pass
    # TODO Add your code here


def are_you_dead(dead):
    """
    Simple function to check if you're dead
    :param dead: A boolean value where false let's the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()


def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.
    :return: None
    """
    global dead             # You'll need this to be able to modify the dead variable
    direction = input("Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(delay)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(delay)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(delay*2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    are_you_dead(dead)


def main():
    """
    The main function, where the program starts.
    :return: None
    """
    user = intro()
    paths = [scott_adventure, team_1_adv, team_2_adv, team_3_adv, team_4_adv, team_5_adv, team_6_adv, team_7_adv, team_8_adv, team_9_adv, team_10_adv, team_11_adv, team_12_adv, team_13_adv, team_14_adv, team_15_adv, team_16_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different
    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list
    end_story(user)


main()

# Adding a comment to demonstrate branching
