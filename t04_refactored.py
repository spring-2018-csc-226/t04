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
    # TODO Add your code here


def team_4_adv():
    pass
    # TODO Add your code here


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


def team_11_adv(direction):
    global dead
    if direction == "North":
        print()
        friend = input("Do you approach the man or run away? [Approach/Run Away]")
    elif direction == "South":
        quit()
    else:
        dead = False
        return dead

    if friend == "Approach":
        print()
        print("Turns out the stranger is feral...")
        print("He tries attacks you savagely.")
        sleep(delay)
        print()
        fight = input("Do you chose to run or fight? [Run/Fight]")
        # For int() feature
    if fight == "Fight":
        print()
        print("The stranger clobbers you with a femur bone from his last victim")
        print("Now the stranger waits for another lost traveler to feast on.")
        dead = True
    # Player Death
    elif fight == "Run":
        print()
        print("You decided to run away but tragically died")
        print("by stumbling on a in the dark and hitting your head...")
        sleep(delay)
        dead = True
    # Player Won Game
    else:
        print()
        print("You weren't thinking correctly and somehow won after a bloody battle.")
        sleep(delay)
        print("Due to sheer luck you survive and stumble out of the darkness!")

    # Crappy Win
    if friend == "Run Away":
        print()
        print("You decided to run way!")
        print("...")
        sleep(delay)
        print("You managed to escape in the darkness...barely. Although")
        print("now you are permanently injured but are found by local towns folk.")
    # Can't decide correctly
    else:
        print("You weren't thinking correctly and died in the stranger's hand...should have\nran away when you can")
    # Brutal Death

    if dead:
        quit()


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
