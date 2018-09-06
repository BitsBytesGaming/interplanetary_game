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
    print("\n" * 1000)
    print("##########################################")
    print("#       Welcome to Interplanetary!       #")
    print("##########################################")
    print("#                - Play -                #")
    print("#                - Help -                #")
    print("#                - Quit -                #")
    print("#         Copyright 2018 BitsBytes       #")
    print("##########################################")
    title_screen_selections()

def help_menu():
    print("\n" * 1000)
    print("##########################################")
    print("#       Welcome to Interplanetary!       #")
    print("##########################################")
    print("# - Use up, down, left, or right to move #")
    print("#  - Type your commands to execute them  #")
    print("#   - Use 'look' to inspect something    #")
    print("#        - Good luck and have fun!       #")
    print("##########################################")
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

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
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

zonemap = {
    'a1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
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
        UP: 'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT: '',
    },
}

### GAME INTERACTIVITY ###
def print_location():
    print('\n' + ("#" * (4 + len(zonemap[myPlayer.location][DESCRIPTION]))))
    print('# ' + myPlayer.location.upper() + ' - ' + zonemap[myPlayer.location][ZONENAME] + ' ' * ((len(zonemap[myPlayer.location][DESCRIPTION]) - len(zonemap[myPlayer.location][ZONENAME])) - 5) + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('#' * (4 + len(zonemap[myPlayer.location][DESCRIPTION])))

def prompt():
    print("\n What would you like to do?")
    action = input("> ")
    acceptable_actions = ['quit', 'exit', 'move', 'go', 'travel', 'quit', 'examine', 'inspect', 'interact', 'look', 'puzzle']
    while action.lower() not in acceptable_actions:
        print("Unknown action, please try again.\n")
        action = input("> ")
    if action.lower() in ['quit', 'exit']:
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['puzzle']:
        player_puzzle(action.lower())

def player_move(myAction):
    ask = "\n In which direction would you like to move?"
    dest = input(ask + "\n> ")
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
    print("\n" + "You have moved to sector " + destination.upper() + ".")
    myPlayer.location = destination
    print_location()

def player_puzzle(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("\nYou have already solved this sector.")
    else:
        print("\nYou can trigger a puzzle here.")

def player_solve(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("This sector has already been solved.")
    else:
        solved_places[myPlayer.location] = True

def player_examine(action):
    print("\n" + "You have examined sector " + myPlayer.location.upper() + ".")
    print("\n" + zonemap[myPlayer.location][EXAMINATION])

def player_loot(action):
    decider = randint(1,10)
    if 

### GAME FUNCTIONALITY ###
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def setup_game():
    print("\n" * 1000)

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
    print('\n' * 1000)

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

    time.sleep(1)
    print("\n" * 1000)
    print("##########################")
    print("#    Let's start now!    #")
    print("##########################")
    main_game_loop()

title_screen()

time.sleep(500)