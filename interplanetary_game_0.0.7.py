import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### PLAYER SETUP ###
class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.bp = 0
        self.vp = 0
        self.job = ''
        self.money = 0
        self.inventory = []
        self.status_effects = []
        self.location = 'c3'
        self.game_over = False
myPlayer = Player()

### TITLE SCREEN ###
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        time.sleep(0.5)
        setup_game()
    elif option.lower() == ("help"):
        time.sleep(0.5)
        help_menu()
    elif option.lower() == ("quit"):
        time.sleep(0.5)
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            time.sleep(0.5)
            setup_game()
        elif option.lower() == ("help"):
            time.sleep(0.5)
            help_menu()
        elif option.lower() == ("quit"):
            time.sleep(0.5)
            sys.exit()

def title_screen():
    title_str1 = ("\n" * 100)
    title_str2 = ("\n##########################################")
    title_str3 = ("\n#       Welcome to Interplanetary!       #")
    title_str4 = ("\n##########################################")
    title_str5 = ("\n#                - Play -                #")
    title_str6 = ("\n#                - Help -                #")
    title_str7 = ("\n#                - Quit -                #")
    title_str8 = ("\n#         Copyright 2018 BitsBytes       #")
    title_str9 = ("\n##########################################\n")
    for character in title_str1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00001)
    for character in title_str2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    for character in title_str3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    for character in title_str4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    for character in title_str5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    for character in title_str6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    for character in title_str7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    for character in title_str8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    for character in title_str9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    title_screen_selections()

def help_menu():
    help_menu_str1 = ("\n" * 200)
    help_menu_str2 = ("\n##########################################")
    help_menu_str3 = ("\n#       Welcome to Interplanetary!       #")
    help_menu_str4 = ("\n##########################################")
    help_menu_str5 = ("\n# - Use up, down, left, or right to move #")
    help_menu_str6 = ("\n#  - Type your commands to execute them  #")
    help_menu_str7 = ("\n#   - Use 'look' to inspect something    #")
    help_menu_str8 = ("\n#        - Good luck and have fun!       #")
    help_menu_str9 = ("\n##########################################\n")
    for character in help_menu_str1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00001)
    for character in help_menu_str2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in help_menu_str3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in help_menu_str4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in help_menu_str5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in help_menu_str6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in help_menu_str7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in help_menu_str8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in help_menu_str9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    title_screen_selections()

### MAP ###
"""
a1 a2... # PLAYER STARTS AT c3
-----------------
|   |   |   |   | a4
-----------------
|   |   |   |   | b4
-----------------
|   |   |   |   | ...
-----------------
|   |   |   |   |
-----------------
"""

ZONENAME = ""
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
LOOTED = False
REPUTATION = 50
KEY = ''
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

looted_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },
    'b4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: '',
    },
    'c1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2',
    },
    'c2': {
        ZONENAME: "The Vulpexi System",
        DESCRIPTION: '',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3',
    },
    'c3': {
        ZONENAME: "The Zolniya System",
        DESCRIPTION: 'The Zolniya system, your point of arrival in this cluster, contains many resources suitable for colonization.',
        EXAMINATION: 'This system seems to undergo very little change over time, or at least none since you last examined it.',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 75,
        KEY:'',
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4',
    },
    'c4': {
        ZONENAME: "00060c",
        DESCRIPTION: '6c 20 65 20 61 20 76 20 65',
        EXAMINATION: 'Upon analysis of data from your scanners, many carbonaceous asteroids have been detected.',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'six',
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: '',
    },
    'd1': {
        ZONENAME: "The Tetranis System",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2',
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'c2',
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3',
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'c3',
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4',
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        LOOTED: False,
        REPUTATION: 50,
        KEY:'',
        UP: 'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT: '',
    },
}

### GAME INTERACTIVITY ###
def print_location():
    location_str1 = ('\n' + ("#" * (4 + len(zonemap[myPlayer.location][DESCRIPTION]))))
    location_str2 = ('\n# ' + myPlayer.location.upper() + ' - ' + zonemap[myPlayer.location][ZONENAME] + ' ' * ((len(zonemap[myPlayer.location][DESCRIPTION]) - len(zonemap[myPlayer.location][ZONENAME])) - 5) + ' #')
    location_str3 = ('\n# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    location_str4 = ('\n' + '#' * (4 + len(zonemap[myPlayer.location][DESCRIPTION])) + '\n')
    for character in location_str1:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.02)
    for character in location_str2:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.02)
    for character in location_str3:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.02)
    for character in location_str4:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.02)
    time.sleep(0.5)

def prompt():
    prompt_str1 = ("\nWhat would you like to do?\n")
    for character in prompt_str1:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
    action = input("> ")
    acceptable_actions = ['quit', 'exit', 'move', 'go', 'travel', 'quit', 'examine', 'inspect', 'interact', 'look', 'puzzle', 'solve', 'loot', 'money', 'credits', 'reputation']
    while action.lower() not in acceptable_actions:
      prompt_str2 = ("\nUnknown action, please try again.\n")
      for character in prompt_str2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
      action = input("> ")
    if action.lower() in ['quit', 'exit']:
      sys.exit()
    elif action.lower() in ['move', 'go', 'travel']:
      player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
      player_examine(action.lower())
    elif action.lower() in ['puzzle']:
      player_puzzle(action.lower())
    elif action.lower() in ['loot']:
      player_loot(action.lower())
    elif action.lower() in ['money', 'credits']:
      player_money(action.lower())
    elif action.lower() in ['reputation']:
      player_reputation(action.lower())

def player_move(myAction):
    movement_handler_str1 = "\nIn which direction would you like to move?"
    for character in movement_handler_str1:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.025)
    dest = input("\n> ")
    acceptable_moves = ['up', 'north', 'down', 'south', 'left', 'west', 'right', 'east']
    while dest not in acceptable_moves:
        move_str1 = "\nUnknown destination, please try again.\n"
        for character in move_str1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        dest = input("\n> ")
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)

def movement_handler(destination):
    movement_str1 = ("\n" + "You have moved to sector " + destination.upper() + ".\n")
    for character in movement_str1:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
    time.sleep(0.5)
    myPlayer.location = destination
    print_location()

def player_puzzle(action):
    puzzle_str1 = ("\nYou have already solved this sector.")
    puzzle_str2 = ("\nYou can trigger a puzzle here.")
    if solved_places[myPlayer.location] == True:
        for character in puzzle_str1:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
    else:
        for character in puzzle_str2:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
        
def player_solve(action):
    solve_str1 = ("\nThis sector has already been solved.")
    solve_str2 = ("\nYou have solved Sector " + myPlayer.location.upper() + " .\n")
    if solved_places[myPlayer.location] == True:
        for character in solve_str1:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
    else:
        solved_places[myPlayer.location] = True

def player_examine(action):
    examine_str1 = ("\nYou have examined sector " + myPlayer.location.upper() + ".")
    examine_str2 = ("\n" + zonemap[myPlayer.location][EXAMINATION] + "\n")
    for character in examine_str1:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
    time.sleep(1)
    for character in examine_str2:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
    time.sleep(0.5)

def player_loot(action):
  loot_str1 = ("\nLooting in progress...")
  for character in loot_str1:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  time.sleep(1)
  loot_decider = random.randint(1,10)
  loot_value = 0
  if loot_decider in [1, 2, 3]:
    loot_value = random.randint(0, 49)
  elif loot_decider in [4, 5, 6, 7]:
    loot_value = random.randint(50, 99)
  elif loot_decider in [8, 9]:
    loot_value = random.randint(100, 149)
  elif loot_decider in [10]:
    loot_value = random.randint(150, 199)
  loot_str2 = "\nYou successfully looted this sector for " + str(loot_value) + " credits.\n"
  myPlayer.money += loot_value
  loot_punish_int = int(int(10^2)/(1+(int(loot_value)^3)))
  loot_str3 = "\nAdditionally, you have lost " + str(loot_punish_int) + " reputation in Sector " + myPlayer.location.upper() + ".\nYou now have " + str(zonemap[myPlayer.location][REPUTATION]) + " reputation in this sector.\n"
  looted_places[myPlayer.location] = True
  loot_punish_bool = random.randint(0,2)
  if loot_punish_bool in [0,1]:
      loot_punish_bool = True
  else:
      loot_punish_bool = False
  for character in loot_str2:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  time.sleep(0.5)
  if loot_punish_bool == True:
      zonemap[myPlayer.location][REPUTATION] -= loot_punish_int
      for character in loot_str3:
          sys.stdout.write(character)
          sys.stdout.flush()
          time.sleep(0.05)
  time.sleep(0.5)

#    else:
#        loot_str4 = "\nYou have already looted this sector.\n"
#        for character in loot_str4:
#          sys.stdout.write(character)
#          sys.stdout.flush()
#          time.sleep(0.05)

def player_money(action):
    money = myPlayer.money
    money_str = "\nYou have " + str(money) + " credits.\n"
    for character in money_str:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
    time.sleep(0.5)

def player_reputation(action):
  reputation = zonemap[myPlayer.location][REPUTATION]
  reputation_str = "\nYou have " + str(reputation) + " reputation in Sector " + myPlayer.location.upper() + ".\n"
  for character in reputation_str:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  time.sleep(0.5)

### GAME FUNCTIONALITY ###
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def setup_game():
    print("\n" * 200)

    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "Hello " + player_name +", what role would you like to play?\n"
    question2added = "(You can play as a warrior, trader or explorer)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(0.5)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ")
    valid_jobs = ['warrior', 'trader', 'explorer']
    if myPlayer.job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job not in valid_jobs:
        player_job = input("> ")
        if myPlayer.job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")

    ### PLAYER STATS ###
    if myPlayer.job is 'warrior':
        self.hp = 100
        self.bp = 60
        self.vp = 20
    if myPlayer.job is 'trader':
        self.hp = 60
        self.bp = 100
        self.vp = 20
    if myPlayer.job is 'explorer':
        self.hp = 60
        self.bp = 20
        self.vp = 100

    ### INTRODUCTION ###
    question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1)
    print('\n' * 200)
    speech1 = "Welcome to this vast galaxy!\n"
    speech2 = "I hope it greets you well!\n"
    speech3 = "Just make sure you don't get lost...\n"
    speech4 = "Heheheh...\n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    time.sleep(2)

    setup_str1 = ("\n" * 200)
    setup_str2 = ("\n##########################")
    setup_str3 = ("\n#    Let's start now!    #")
    setup_str4 = ("\n##########################")
    setup_str5 = ("\n" * 200)
    for character in setup_str1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00001)
    for character in setup_str2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in setup_str3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in setup_str4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

    time.sleep(1)

    for character in setup_str5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.00001)

    main_game_loop()

title_screen()