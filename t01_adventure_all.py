######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
#
# Assignment: T1: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

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
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)


if dead == True:
    quit()


#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-anne-joseph

if direction == "East":
    #Bravo!
    print("You are in front of Building 1 and Building 2, both are gigantic and luxurious.")
building = input("Which building would you pick? [Building1/Building2]")
if building == "Building1":
    #smart choice
    print("Seems someone has a surprise for you..")
    print("WOW! Welcome to the wonderland where you will be presented a 32 carat diamond Worth $150,000.")
elif building == "Building2":
    #Bad choice
    print("Welcome to the dragon's home where no one ever survives.")
    print("You are trying to escape, but the door behind you is already shut automatically, you have no option but wait on the dragon.")
    dead = True
if dead == True:
    quit()

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-tayttum-aden


direction = input("The squirrel asks you 'WHICH PATH WILL YOU TAKE?!'[Right, Left or Straight]")

if direction == "Straight":
    # Good choice!
    print("You are still trapped in the blizzard, but something else is there with you now! Let's hope they like humans.")
    print("You move along in the forest and you approach a jackass penguin.")
    print("The jackass penguin greets you by saying, 'hello darling, are you lost?'")
    print("You reply saying 'yes' as you've never been here before and the penguin nods")
    print("The penguin agrees to help you, and hops on your shoulder")
    print("You eventually make it to the mysterious world where you are greeted by talking animals.")
    print("You are crowned king or queen by a dog")
    print("To be continued")
    sleep(delay)

elif direction == "Left":
    # Oh... Bad choice
    print("You hear a roar. Not a tiny roar, but a large Growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Ooo no. Turns out the forest was home to a Killer Fluffy Bunny.")
    print("You want to run away. But... it's raining, and pitch black.")
    print("You turn and run like hell anyways. The bunny wakes up to the sound of your feet pounding against the wet earth.")
    print("The bunny reaches you and eats you alive.")
    print("The story ends in your death, YOU CHOSE WRONG!")
    dead = True
else:

    # Neutral choice
    print("You're in another part of the forest. It is now windy, and very dark. 'Please get me out of here!'")
    print("You move along in the forest and you approach a jackass penguin.")
    print("The jackass penguin greets you by saying, 'hello dear, are you lost?'")
    print("You reply saying 'yes' as you've never been here before and the penguin nods")
    print("The penguin rolls his eyes 'Incompetent humans now days, follow me' and he walks off")
    print("You follow the penguin and eventually make it to the edge of the forest, where you see a red door.")
    print("To be continued")
    sleep(delay)


if dead == True:
    quit()
#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-cohen

response = input ("The true love of your life awaits at the bottom of the stairs. Time is short, and you must whisper something in his/her ear. How does s/he respond? [cry / embrace / laugh]")

while response not in ["cry", "embrace", "laugh"]:
    response = input ("You have chosen a destiny that is beyond the boundaries of the mind. You are incomprehensible. You stare blankly ahead. \nThe true love of your life awaits at the bottom of the stairs. Time is short, and you must whisper something in his/her ear. How does s/he respond? [cry / embrace / laugh]")
if response == "cry":
    print("Your resolve weakens and you find yourself unable to kill him. You sign the document, and your fate is sealed.")
    dead = True
    sleep(delay)

elif response == "embrace":
    print("You stab him in the thigh, and vengeance is yours! You step over his gory body and walk out of the house...")
    sleep(delay)

else:
    print("You discover to your chagrin that you cannot enact your plan immediately. You turn and use the knife on the parsnips and yams. How disappointing, but the romance continues...")
    sleep(delay)

second_question = int(input("After weeping your harbor of salty tears and feeling them dry on your cracked cheeks,John Waters style, you decide to bide your time before your next attempt. How long do you wait? [length in days]"))

if second_question < 2:
    print("In your rush to get out of this terrible horrible no good situation, you let your plan be discovered. Oops.")
    dead = True
    sleep(delay)

elif second_question >= 7:
    print ("You conniving, meretricious, deceptive, dissembling, disingenious, duplicitous shark! You win. Muhuhahahah. On to your next victim.")
    sleep(delay)

else:
    print ("You are just not quite sure yet about how to proceed. Better keep on truckin'.")
    sleep(delay)



if dead==True:
    quit()
#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-berucha-susan

print()
sleep(delay)
print("You now have three doors in front of you. The first door says, 'ULTIMATE DEATH'. The second door says, 'FREEDOM'. The last door say, 'HAPPINESS AWAITS'.")
door = input("Which door do you dare pick? [First/Second/Third]")
sleep(delay)

print()
if door == "First":
#Good Choice!
    print("Hahaha, you Daredevil!")
    print("You cannot be fooled.. or were you ready for this story to be over?")
    print("Either way, you have found your way to FREEDOM!")
    sleep(delay)

    print()
elif door == "Second":
#Ohhh, better luck next time!
    print("Ahhhh...")
    print("Did I say 'Freedom'??")
    print("I meant DEATH!!!")
    print("You enter through the door and fall into lava.")
    print("Look on the bright side, at least you died quickly!")
    dead = True
    sleep(delay)

    print()
else:
#Neutral choice
    print("You enter through the door and you are in a land of puppies and kitties! Lucky you!")
    print("Told you happiness awaits!")
    print("However, the door disappears behind you and now you have to still find your way out to freedom.")
    print("Hope you don't have allergies!")
sleep(delay)

if dead == True:
    quit()

print("Good luck on your next adventure!")
# TODO Don't forget to check if your user is dead at the end of your chapter!

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-natasha-ricardo-and-john

# The next chapter.
direction = input("Which direction would you like to go now? [North/South/East/West]")

if direction == "West":
    # Good choice.
    print("You have found food. Now you might not starve to death. Congratulations.")
    sleep(delay)
elif direction == "North":
    # Bad choice.
    print("Suddenly you hear a rumbling above you. You look up to see a falling bolder.")
    sleep(delay)
    number = float(input("Choose a number to determine your fate. [1-10]"))
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

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-annette-and-azah

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
    #Hope you're not too afraid of spiders...
    print("You decided to go to the left, where a narrow rock ledge leads around the corner.")
    print("You follow the ledge, and discover a staircase going up the mountain.")
    print("Your curiosity overcomes you, and you decide to climb up the staircase.")
    sleep(delay)
    dead = False
elif direction == "Right":
    #So sad to die so close to the ground.
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
    #Neutral choice
    print("Paralyzed by indecision, you said in the opening of the tunnel, looking out.")
    sleep(delay)
    print("The sun sets on your hopes and dream.")
    dead = False

# TODO Don't forget to check if your user is dead at the end of your chapter!

if dead == True:
    quit()

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-arlee-and-bethanie

direction = input("Would you like to go deeper into the cave or back to beginning?[deeper/back to beginning]")

if direction == "deeper":
#ohhh... good choice

    print("You find two paths one east and one west.")
    sleep(delay)
    direction = input("Which do you pick? [east/west]")

    if direction == "west":
        #good choice
         sleep(delay)
         print("There is a torch lighting up the cavern you find yourself in.")
         sleep(delay)
         print()
         print("You pick up the torch so it can help you navigate your way through the darkness.")
         sleep(delay)

    elif direction == "east":
        #bad Choice
        print("There is a torch on the wall. You pick it up to help you navigate through the dark.")
        sleep(delay)
        print()
        print("In the light of the torch you can see a shiny object.")
        print()


        direction = input ("Do you want to pick up object or ignore object? [pick up object/ignore Object]")
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

        if dead == True:
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
    #neutral choice
    print("You decide to return to the beginning of your adventure.")
    quit()
# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-david-sahet


if direction == "North":
    # Changes variable direction to enter the next block of conditionals.
    direction = input ('What do you want to do next? [Ask for help/Run]')

if direction == "Ask for help":
    # Good choice
    print("You told them about treasure and asked for company.You told them if you find treasure, you would agree to give them half")
    print("They agreed to go with you as long as you agree to split up treasure")
    sleep(delay)
    print("After searching long time, fortunately, you found treasure under rocks")
    print("You and your partner split the treasure and the two of you make your way to exit of the cave")
    dead = True

elif direction == "Run":
    # Bad choice
    print("You decide that that person was too frightening and decided to run for your life.")
    print ("It's so dark and you can't see. You trip over a loose rock and fall into a ditch.")
    print("Your ankle is sprained and you are unable to walk. Reluctantly, you take out your mobile phone and call a friend for help.")
    print("Your friend arrives and eventually finds you hours later. He helps you out of the ditch and you go home empty-handed. :(")
    dead = True
else:
    #Neutral Choice
    print("You start to get bored and hungry while running around aimlessly in the dark")
    sleep(delay)
    print("After searching for a few hours with no luck, you decide to make your way towards the exit and go home for the day")
    print("Although you didn't find your treasure this time, you can always come back during your free time and keep searching")
    dead = True
if dead == True:
    quit()

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-eli-robert

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

if choice == "pick up hat":
    print("It's a trap! You were forced to attend Berea College for 4 years, get a decent job, and died at the age of 102.")
    dead = True
elif choice == "sit in chair":
    print("You sit in the chair and you wake up 3 hours later, you just wasted 3 hours")
elif choice == "walk away":
    print("As you walk away, you find some sneakers with +5 jump on your path.")
    sleep(delay*2)
    print("You try to jump with your new +5 sneakers, you jump and quickly find yourself free from the gravity, your journey should go mush quicker now.")

# Don't forget to check if your user is dead at the end of your chapter!
if dead == True:
    quit()

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-erin-ezra

print("You encounter a set of three doors, which door do you take? [Door 1/Door 2/Door 3]")
direction = input()

if direction == "Door 1":
    print("You have selected Door 1.")
    print("There is a path that leads you further in your quest.")
elif direction == "Door 2":
    print("You have selected Door 2.")
    print("Oh no! There's a man-eating goat!")
    print("If you can guess his favorite number, then he will not eat you.")
    num_guess = int(input("What do you think it is?"))
    if num_guess <= 8 and num_guess >= 8:
        print("The goat is impressed with your knowledge of astrology, a skill that totally has an actual purpose.")
        print("He tells you the path lies behind Door 1, and you continue on your quest.")
    elif num_guess > 8:
        print("The goat is angered by your audacity at such an invalid attempt. I'm sorry, but he has eaten you. :(")
    else:
        print("The goat is angered by your ignorance. I'm sorry, but he has eaten you. :(")
        dead = True
else:
    print("That was a strange choice.")
    print("There's a goat. He is now your companion.")
    print("Please select one of the other doors. [Door 1/Door 2]")
    direction = input()

    if direction == "Door 1":
        print("You have selected Door 1.")
        print("There is a path that leads you further in your quest.")
    elif direction == "Door 2":
        print("You have selected Door 2.")
        print("Oh no! There's a man-eating goat!")
        print("If you can guess his favorite number, then he will not eat you.")
        num_guess = int(input("What do you think it is?"))
        if num_guess <= 8 and num_guess >= 8:
           print("The goat is impressed with your knowledge of astrology, a skill that totally has an actual purpose.")
           print("He tells you the path lies behind Door 1, and you continue on your quest.")
        elif num_guess > 8:
            print("The goat is angered by your audacity at such an invalid attempt. I'm sorry, but he has eaten you. :( He left your goat though!")
        else:
            print("The goat is angered by your ignorance. I'm sorry, but he has eaten you. :( He left your goat though!")
            dead = True
    else:
        print("Your goat companion decided you should go through Door 1.")
        print("There is a path that leads you further in your quest.")

if dead == True:
    quit()

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-cortesj-brownky

if direction == "North":
    print()
    friend = input("Do you approach the man or run away? [Approach/Run Away]")
elif direction == "South":
    quit()


if friend == "Approach":
    print()
    print("Turns out the stranger is feral...")
    print("He tries attacks you savagely.")
    sleep(delay)
    print()
    Fight = input("Do you chose to run or fight? [Run/Fight]")
    #For int() feature
    if Fight == "Fight":
        print()
        print("The stranger clobbers you with a femer bone from his last victim")
        print("Now the stranger waits for another lost traveler to feast on.")
        dead = True
    #Player Death
    elif Fight == "Run":
        print()
        print("You decided to run away but tragically died")
        print("by stumbling on a in the dark and hitting your head...")
        sleep(delay)
        dead = True
    #Player Won Game
    else:
        print()
        print("You weren't thinking correctly and somehow won after a bloody battle.")
        sleep(delay)
        print("Due to sheer luck you survive and stumble out of the darkness!")

# Crappy Win
elif friend == "Run Away":
    print()
    print("You decided to run way!")
    print("...")
    sleep(delay)
    print("You managed to escape in the darkness...barely. Although")
    print("now you are permenantly injured but are found by local towns folk.")
#Can't decide correctly
else:
    print("You weren't thinking correctly and died in the stranger's hand...should have\nran away when you can")
#Brutal Death


# TODO Don't forget to check if your user is dead at the end of your chapter!

if dead == True:
    quit()

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-kaleb-robinson-siso-mashilo

print ()
print ("Warrior you have now entered the belly of the beast")
action = input("Be ready to battle, choose a weapon [Sword/ Thor's hammer/ Shield/]")

if action == "Sword":
    # Great you're like King arthur now!
    # Neutral choice
    print("A cage door closes behind you. You hear a large roar in the darkness. You unsheathe your sword to fight. Ahead of you is a giant firebreathing dragon.")
    sleep(delay)
    print ("You look onto the beast with hesitation. You simply have no defense.")
    dead = True
elif action == "Thor's hammer":
    # Oh... Bad choice
    print("A cage door opens behind you. You hear a large roar in the darkness.")
    sleep(delay)
    print("You reach for thor's hammer, but struggle to lift it. A large fireball blasts through the darkness and roasts you alive. ")
    print("END: YOU ARE UNWORTHY.")
    dead = True
elif action == "Shield":
    # Neutral choice
    print("You draw your shield. A cage door closes shut behind you. In front of you emerges a firebreathing dragon.")
    sleep(delay)
    shieldaction=input('What does the warrior do? Flee or Stand your ground? [Flee/ Stand]')
    if shieldaction== "Flee":
        print("You run to the other side of the arena, ducking behind pillars and dodging fireballs.")
        sleep(delay)
        sleep(delay)
        print("You find another door covered in a cage. You grasp and pull the cage to no avail. Suddenly you feel warm breath on the back of your neck. You close your eyes and give a prayer to the gods.")
        dead = True
    elif shieldaction== "Stand":
        print ("You stand tall against the large threat. The monster breathes fire around you, but you block it with your shield")
        sleep (delay)
        print ("There is fire all around. It begins to puncture your weak shield slowly draining your health.")
        sleep(delay)
        sleep (delay)
        print ("Hp=9")
        print ('8,7,6,5,4,3,2,1')
        sleep (delay)
        sleep (delay)
        sleep (delay)
        print ("In a last desperate act of life you throw your shield in the direction of the flame. It lodges into the monsters throat, killing him instantly.")
        print ("The cage door opens you are free.")
        # YAY you live!
        dead= False

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-giorgi-lomia-robert-hogsed


print()
print(username, " in front of you, you see a cliff of unconquerable proportions")
sleep(delay*2)
print()
print("behind you, you can hear a noise, you have never heard before,")
print("it scares you more then anything")
print("you also spot darkness a bit left of you.")
print()
print(username, " you have options, climb the cliff, go down into the darkness,")
print("or face whatever terrifies you by its mere sound")
sleep(delay*3)
direction = input("Where do you want to go [Up/Down/Stay]")

if direction == "Up":
    print(username, " I just told you it was gigantic, why would you do this?")
    print()
    print("you start climbing the cliff, adrenaline is pumping through your veins" )
    sleep(delay*2)
    print()
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
    print("You crawl into the darkness.")
    sleep(delay)
    print()
    print("You feel as if you have been crawling forever, but you begin to see a light in the darkness")
    print("as you get closer to the light, you begin to feel a breeze")
    print()
    sleep(delay)
    print("As you reach the light you realize it is an exit to the cave, you have made it to safety")
else :
    print("Whatever was making that noise, it begins to get closer")
    print(" Your palms are sweaty, knees weak, arms are heavy")
    sleep(delay*2)
    print()
    print("You begin to smell something quite pleasant, you turn to look over your shoulder")
    print("There standing before you is a chimpanzee carrying a hot plate of spaghetti")
    print()
    sleep(delay*2)
    print("He approaches you and offers the spaghetti to you before going in for a nice big hug.")
    print()
    print("The monkey decides to join you in your adventure")

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-taran-ahad-gerardo


print("You've come to across two separate tunnels.")
print()
direction = input("Which way do you go? (Left/Right/Go Back)")
if direction == "Left":
    #Bad choice
    print("OH NO! The cave collapsed behind you. You'll survive for two more days before dying from lack of oxygen.")
    dead = True

elif direction == "Right":
    #Good choice
    print(username , "found a sandwich, gained 10 HP.")

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

#########################################################################################################
# https://github.com/spring-2018-csc-226/t1-choose-your-own-adventure-miranda-flannery-montana-hite

print()
print("Due to a mysterious person in the cave (whether or not you've met them yet),")
print("you teleport immediately out of any given situation you're in. You now stand")
print("at the entrance to the cave. It's pretty out.")
print()
print("In front of you is a path. One way leads to a river, and the other is so beaten that")
print("That you would defintely get lost if you tried to use it.")
print("However, the cave you have recently were forced out of now glows... weird.")
decision = input("Where do you go? [Woods/River/Cave]")

if decision == "River":
    print("")
    print("You decide to head towards the river. It feels... familiar to you.")
    print("After following the river for a while, you come across a small boat.")
    print("It looks like a fisherman's boat, but the fisherman isn't around.")
    boat_choice = input("Take the boat?[Y/N]")
    if boat_choice == "Y":
        print("")
        print("You take the boat and ride to the nearest freedom!")
        print("However, a new danger is on the horizon...")
    else:
        print("")
        print("Look at that! You're NOT a thief?")
        print("You continue walking down the river in hopes of finding... something.")
        print("You feel like, ultimately, you should have taken the boat. Hindsight's 20/20.")


elif decision == "Cave":
    print("")
    print("You're not sure what's come over you, but you feel the desire to go BACK into the cave.")
    print("(Moron.)")
    print("")
    print("Guarding the front of the cave now is the mystic dragon protector.")
    print("It should go without saying that you're not a high enough level to beat it.")
    print("However, you could try to speak to it. I bet it speaks English, right?")
    dragon_decision = input("Do you commune with the dragon? [Y/N] ")
    if dragon_decision == "Y":
        print("")
        print("The dragon lowers its head to you and billows great smoke.")
        print('"Before you can pass, you must guess how many scales I have?"')
        scale_number = int(input("What is your guess?"))
        if scale_number >= 226:
            print("")
            print("Dragon moves slightly out of the way and you proceed further into the cave.")
        else:
            print("")
            print('"Wrong answer."')
            print(" The dragon barbeques you, throws you up in the air, and swallows you whole.")
            dead = True
    else:
        print("")
        print("At your attempt to leave the cave, the dragon stops you and eats you.")
        print("Sorry bud.")
        dead = True

else:
    print("")
    print("You decide to go follow the beaten path deeper into the woods.")
    print("In front of you is a group of bandits. Finding that you have no valuables,")
    print("They decide to take you hostage! Good luck, bud.")
    print("Well, at least you're not dead.")


if dead == True:
    quit()


#########################################################################################################






