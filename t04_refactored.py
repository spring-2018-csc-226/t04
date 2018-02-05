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
    pass
    # TODO Add your code here


def team_2_adv():
    pass
    # TODO Add your code here


def team_3_adv():
    pass
    # TODO Add your code here


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():
    pass
    # TODO Add your code here


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
    pass
    # TODO Add your code here


def team_10_adv():
    pass
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
    pass
    # TODO Add your code here


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
