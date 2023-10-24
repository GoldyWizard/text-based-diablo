print("What's your name?")
pl_name = input(">>> ")
pl_class = "empty"
confusion: False
death = False
c1, c2, c3, = False, False, False

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("Choose your class: ")
print("|Slayer|"+" "+"|Rogue|"+" "+"|Warrior|")
pl_class = input(">>> ")
if pl_class == "Slayer" or pl_class == "slayer":
    c1 = True
elif pl_class == "Rogue" or pl_class == "rogue":
    c2 = True
elif pl_class == "Warrior" or pl_class == "warrior":
    c3 = True

if c1 or c2 or c3 == True:
    print("Excellent!")
else:
    print("Hmm? What is that?")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
print("Welcome to Tristram,"+" "+pl_class.capitalize()+" "+pl_name.capitalize()+" stay awhile and listen! Will you help us?")
ans = input("Y/N? >>> ")
print(" ")
if ans == "y": 
    print("Thank you! Slay Diablo in the old church!")
    print(" ")
elif ans == "n":
    death = True
    print("Then you must leave...")
    print("|Leave| ")
    input(">>> ")
else:
    confusion = True

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// 
health = 100
mana = 10
t1 = "alpha"
print(">You enter the old church, the smell of blood permeates the air.")
if death == False or confusion == False:
    print("You seem to hear scurrying, then a low roar and deep voice saying:")
    print("Fresh meat!")
    print(" ")
    print("What will you do?!")
    print(" ")
    print(("|Fight|"+" "+"|Run|")) 
    t1 = input(">>> ")

if t1 == "fight":
    print("|Bronze Sword| ")
    t1 = input(">>> ")

if t1 == "attack":
    print("You swing your sword! Only to be cleaved in two by The Butcher...")
    death = True 
else:
    confusion = True

if t1 == "run":
    print("You turn tail and make for the stairwell back up! Only to be pierced by a hook and reeled in to The Butcher's maw...")
    death = True
else:
    confusion = True

if death == True:
    print(" ")
    print("Death takes you...")
    print("Diablo consumes all...")
elif confusion == True:
    print(" ")
    print("Dementia takes you...")
    print("Diablo consumes all...")

print(" ")
print("Thank you for playing!")

# 1:36am - Try to make it so that whenever you press enter, it'll throw an error message.
# Try to also make it to have an "end the game" command so you don't have to go through the whole thing to kill it.
# Try to implement a save at some point?
# Add more classes
# Add equipment
# Add a shop
# Add NPCS
# Add colored text
# Clean up the code if you can
# Make the code loop after game ends, so the program won't quit