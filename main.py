#imports
from replit import db
from random import randint
import time
#Variables
playerMaxHealth = 0

# funcs
def menu():
  print("1. start game")
  print("2. Settings")
  print("3. exit")
  choice = input("(Use the number of the option)\n what would you like to do? ")

  if choice == "1":
    game()
  elif choice == "2":
    print("this is the settings menu")
  elif choice == "3":
    exit()
  else:
    print("you did not enter a valid option")

def fight(hp, dmg,):
  print("fight")

def game():
  print('1. warrior ') #100hp dmg??
  print("2. archer ")  #80hp  dmg??
  print("3. mage ") #60hp     dmg??
  print("4. summoner ") #40hp dmg??
  print("5. tanker ") #300hp  dmg??
  playerClass = input('What class you wanna be Select the number')
  if playerClass == 1:
    print ("now you have 150hp")
  elif playerClass == 2:
    print("now you have 90hp")
    playerMaxHealth = 90
  elif playerClass == 3:
    print("now you have 90hp")
    playerMaxHealth = 90
  elif playerClass == 4:
    print("now you have 80hp")
    playerMaxHealth = 80
  elif playerClass == 5:
    print("now you have 150hp")
    playerMaxHealth = 250
  print("""
  1.fight
  2.menu""")
  selection = input("Select what do you want to do")
  if selection == "fight":
    fight(randint(1,10), randint(1, 100))
  elif selection == "menu":
    menu()

#intro
print("Welcome to TBRPG\nGAME SUBJECT IS TO CHANGE")
print()
print("This is a text based rpg game")
#namesaving
playerName = input("give a name for your player: ")
#test
if playerName == "Tests":
  import os
  os.system("python tests.py")
  exit()
print("this name will be used to mention you in game")
print()
print("you can change this name later")
print()
#menu
menu()