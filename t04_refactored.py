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
user = ""
dead = False


def intro():
    """
    Introduction text for the story. Don't modify this function
    :return: None
    """
    global user                            # You need this to be able to modify the user's name
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


def end_story():
    """
    This is the ending to the story. Don't modify this function, either.
    :return: None
    """
    print("Congratulations, you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay*5)
    print("Now go away.")


def table_1_adv():
    pass
    # TODO Add your code here


def table_2_adv():
    pass
    # TODO Add your code here


def table_3_adv():
    pass
    # TODO Add your code here


def table_4_adv():
    pass
    # TODO Add your code here


def table_5_adv():
    pass
    # TODO Add your code here


def table_6_adv():
    pass
    # TODO Add your code here


def table_7_adv():
    pass
    # TODO Add your code here


def table_8_adv():
    pass
    # TODO Add your code here


def table_9_adv():
    pass
    # TODO Add your code here


def table_10_adv():
    pass
    # TODO Add your code here


def table_11_adv():
    pass
    # TODO Add your code here


def table_12_adv():
    pass
    # TODO Add your code here


def table_13_adv():
    pass
    # TODO Add your code here


def table_14_adv():
    pass
    # TODO Add your code here


def table_15_adv():
    pass
    # TODO Add your code here


def table_16_adv():
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
        print(user, ", you are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
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
    intro()
    paths = [scott_adventure, table_1_adv, table_2_adv, table_3_adv, table_4_adv, table_5_adv, table_6_adv, table_7_adv, table_8_adv, table_9_adv, table_10_adv, table_11_adv, table_12_adv, table_13_adv, table_14_adv, table_15_adv, table_16_adv]                # TODO Add your function name to the list
    random.shuffle(paths)                               # Shuffles the order of paths, so each run is different
    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story()


main()
