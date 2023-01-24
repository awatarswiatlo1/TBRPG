#imports
from replit import db
from random import randint
import time
# funcs
def game():
  playerMaxHealth = 0
  playerinventory = []
  
  
  playerClass = input('What class you wanna be Select the number')
  print('1. warrior ')
  print("2. archer ")
  print("3. mage ")
  print("4. summoner ")
  print("5. ")
  if playerClass == 1:
    playerMaxHealth = 150
  elif playerClass == 2:
    print("wip")
    
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
