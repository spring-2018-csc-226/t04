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
    direction = input("The squirrel asks you 'WHICH PATH WILL YOU TAKE?!'[Right, Left or Straight]")

    if direction == "Straight":
        # Good choice!
        sleep(delay)
        print("\nYou are still trapped in the blizzard, but something else is\n"
              "there with now! Let's hope they like humans\n"
              "You move along in the forest and you approach a jackass penguin\n"
              "The jackass penguin greets you by saying, 'hello darling, are you lost?\n"
              "You reply saying 'yes' as you've never been here before and the penguin nods\n"
              "The penguin agrees to help you, and hops on your shoulder\n"
              "You eventually make it to the mysterious world where you are greeted by talking animals.\n"
              "You are crowned king or queen by a dog\n"
              "To be continued\n")
        sleep(delay)

    elif direction == "Left":
        # Oh... Bad choice
        print("\nOoo no. Turns out the forest was home to a Killer Fluffy Bunny.\n"
              "You want to run away. But... it's raining, and pitch black.\n"
              "You turn and run like hell anyways. The bunny wakes up to the sound of your feet pounding against the wet earth.\n"
              "The bunny reaches you and eats you alive.\n"
              "The story ends in your death, YOU CHOSE WRONG!\n")
        dead = True
    else:
        # Neutral choice
        print("\nYou're in another part of the forest. It is now windy, and very dark. 'Please get me out of here!'\n"
              "You move along in the forest and you approach a jackass penguin.\n"
              "The jackass penguin greets you by saying, 'hello dear, are you lost?'\n"
              "You reply saying 'yes' as you've never been here before and the penguin nods\n"
              "The penguin rolls his eyes 'Incompetent humans now days, follow me' and he walks off\n"
              "You follow the penguin and eventually make it to the edge of the forest, where you see a red door.\n"
              "To be continued\n")
        sleep(delay)


if dead:
    quit()


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


    direction = input("Would you like to go deeper into the cave or back to beginning?[deeper/back to beginning]")

    if direction == "deeper":
        # oh... good choice

        print("You find two paths one east and one west.")
        sleep(delay)
        direction = input("Which do you pick? [east/west]")

        if direction == "west":
            # good choice
            sleep(delay)
            print("There is a torch lighting up the cavern you find yourself in.")
            sleep(delay)
            print()
            print("You pick up the torch so it can help you navigate your way through the darkness.")
            sleep(delay)

        elif direction == "east":
            # bad Choice
            print("There is a torch on the wall. You pick it up to help you navigate through the dark.")
            sleep(delay)
            print()
            print("In the light of the torch you can see a shiny object.")
            print()
            direction = input("Do you want to pick up object or ignore object? [pick up object/ignore Object]")
            if direction == "pick up object":
                sleep(delay)
                print("The object is a large golden lamp.")
                print()
                print("You rub the lamp and a colorful smoke spills out of the spout.")
                sleep(delay)
                print("The smoke stinks and you are feeling sleepy.")
                print()
                sleep(delay)
                print("You fall asleep instantly and hit your head on the cave floor.")
                print()
                sleep(delay)
                print("You are dead.")

            if dead:
                quit()

            if direction == "ignore object":
                sleep(delay)
                print("You see a light through a crack in the cave wall.")
                print("You walk towards it and kick the rubble that was blocking the light.")
                sleep(delay)
                print()
                print("You crawl out of the cave blinking in the bright sunlight. You are free at last.")
                print()
                print("Congratulations!")


    if direction == "back to beginning":
        # neutral choice
        print("You decide to return to the beginning of your adventure.")
        quit()


def team_8_adv():

    # TODO Add your code here
    global dead
# Team 8

    direction = input('What do you want to do next? [Ask for help/Run]')

    if direction == "Ask for help":
        # Good choice
        print()
        print("You told them about treasure and asked for company.You told them if you find treasure, you would agree to give them half")
        print("They agreed to go with you as long as you agree to split up treasure")
        print()
        sleep(delay)
        print("After searching long time, fortunately, you found treasure under rocks")
        print("You and your partner split the treasure and the two of you make your way to exit of the cave")

    elif direction == "Run":
        # Bad choice
        print()
        print("You decide that that person was too frightening and decided to run for your life.")
        print()
        print("It's so dark and you can't see. You trip over a loose rock and fall into a ditch.")
        print("Your ankle is sprained and you are unable to walk. Reluctantly, you take out your mobile phone and call a friend for help.")
        print()
        print("Your friend arrives and eventually finds you hours later. He helps you out of the ditch and you go home empty-handed. :(")
        dead = True

    else:
        # Neutral Choice
        print()
        print("You start to get bored and hungry while running around aimlessly in the dark")
        sleep(delay)
        print()
        print("After searching for a few hours with no luck, you decide to make your way towards the exit and go home for the day")
        print("Although you didn't find your treasure this time, you can always come back during your free time and keep searching")

    if dead:
        quit()



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
    pass
    # TODO Add your code here


def team_11_adv():
    global dead
    direction = input("Which direction do you want to go?")
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
    global dead
    print()
    print("Warrior you have now entered the belly of the beast")
    action = input("Be ready to battle, choose a weapon [Sword/ Thor's hammer/ Shield/]")

    if action == "Sword":
        # Great you're like King arthur now!
        # Bad choice
        print("A cage door closes behind you. You hear a large roar in the darkness. You unsheathe your sword to fight. Ahead of you is a giant firebreathing dragon.")
        sleep(delay)
        print("You look onto the beast with hesitation. You simply have no defense.")
        dead = True
    elif action == "Thor's hammer":
        # Oh... Bad choice
        print("A cage door opens behind you. You hear a large roar in the darkness.")
        sleep(delay)
        print("You reach for thor's hammer, but struggle to lift it. A large fireball blasts through the darkness and roasts you alive. ")
        print("END: YOU ARE UNWORTHY.")
        dead = True
    elif action == "Shield":
        # Good choice
        print("You draw your shield. A cage door closes shut behind you. In front of you emerges a firebreathing dragon.")
        sleep(delay)
        shieldaction = input('What does the warrior do? Flee or Stand your ground? [Flee/ Stand]')
        if shieldaction == "Flee":
            print("You run to the other side of the arena, ducking behind pillars and dodging fireballs.")
            sleep(delay)
            sleep(delay)
            print("You find another door covered in a cage. You grasp and pull the cage to no avail. Suddenly you feel warm breath on the back of your neck. You close your eyes and give a prayer to the gods.")
            dead = True
        elif shieldaction == "Stand":
            print("You stand tall against the large threat. The monster breathes fire around you, but you block it with your shield")
            sleep(delay)
            print("There is fire all around. It begins to puncture your weak shield slowly draining your health.")
            sleep(delay)
            sleep(delay)
            print("Hp=9")
            print('8,7,6,5,4,3,2,1')
            sleep(delay)
            sleep(delay)
            sleep(delay)
            print("In a last desperate act of life you throw your shield in the direction of the flame. It lodges into the monsters throat, killing him instantly.")
            print("The cage door opens you are free.")
            # YAY you live!
            dead = False
    else:
        print("That was not an option.")
        return None

    if dead == True:
        quit()


def team_13_adv():
    global dead

    sleep(delay*2)
    print("In front of you, you see a cliff of unconquerable proportions \n")
    print("behind you, you can hear a noise, you have never heard before,")
    print("it scares you more then anything \n")
    print("you also spot darkness a bit left of you. \n")
    print("You have options, climb the cliff, go down into the darkness,")
    print("or face whatever terrifies you by its mere sound")
    sleep(delay*3)
    direction = input("Where do you want to go [Up/Down/Stay]")

    if direction == "Up":
        print("I just told you it was gigantic, why would you do this? \n")
        print("you start climbing the cliff, adrenaline is pumping through your veins \n")
        sleep(delay*2)
        print("You climb it with ease, but halfway up the cliff you look down,")
        print("you realize, that you need to calm your nerves, otherwise you will fail,")
        rest_time = int(input("How many seconds do you want to wait"))

        if rest_time <= 10:

            print("You rest for ",rest_time," seconds")
            print("you sooth your nerves and reach the top you survive")

        else:
            print("you grow tired and your hands loose the grip.")
            print("the height scares you so bad you have a heart attack and fall to your death")
            print("Oh there goes gravity")
            dead = True
    elif direction == "Down":
        print("You crawl into the darkness. \n")
        sleep(delay)
        print("You feel as if you have been crawling forever, but you begin to see a light in the darkness")
        print("as you get closer to the light, you begin to feel a breeze \n")
        sleep(delay)
        print("As you reach the light you realize it is an exit to the cave, you have made it to safety")
    else:
        print("Whatever was making that noise, it begins to get closer")
        print("Your palms are sweaty, knees weak, arms are heavy \n")
        sleep(delay*2)
        print("You begin to smell something quite pleasant, you turn to look over your shoulder")
        print("There standing before you is a chimpanzee carrying a hot plate of spaghetti \n")
        sleep(delay*2)
        print("He approaches you and offers the spaghetti to you before going in for a nice big hug. \n")
        print("The monkey decides to join you in your adventure...")
    if dead:
        quit()


def team_14_adv():
    global dead
    print("You've come across two separate tunnels.")
    print()
    direction = input("Which way do you go? (Left/Right/Go Back)")
    if direction == "Left":
        # Bad choice
        print("OH NO! The cave collapsed behind you. You'll survive for two more days before dying from lack of oxygen.")
        dead = True

    elif direction == "Right":
        # Good choice
        print("You found a sandwich and gained 10 HP which will help you survive longer. Way to go!")

    elif direction == "Go Back":
        # Neutral choice
        print("Tsk, tsk. You chickened out! Now you're stuck still wandering the cave.")

    else:
        # mystery path if user chooses none of the given options
        print("You find a wall with a pin lock on it.")
        pin = int(input("Please enter a number 0-100"))
        if pin >= 50:
            print("You enter the wrong pin! The walls close in around you and you die.")
            dead = True
        elif pin <= 49:
            print("A secret door opens itself to you and you continue deeper into a mysterious abyss.")
    if dead:
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
