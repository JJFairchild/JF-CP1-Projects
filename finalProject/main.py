#Jonas Fairchild, Final Project

try: #Checks if the keyboard is installed and does not run the rest of the program if not.
    import keyboard
    moveError = True
except:
    print("Please install the keyboard by typing 'pip3 install keyboard' into the terminal before playing.")
    moveError = False

if moveError:
    playerName = input('Select a one-character name for your player: ')
    while len(playerName) != 1:
        print('Invalid player name. Try again.')
        playerName = input('Select a one-character name for your player: ')

blockTypes = ['▮', '▯', 'v', '^', '>', '<', 'C', playerName, 'E']
enemies = [[100, [['use sword', 30]]]]
health = 100
import random
playerPos = [0, 0]
gravity = 0.25
velocity = [0, 0]
coins = 0
import time
map = [playerPos, 7, [-1, -2], 0, [0, -2], 0, [1, -2], 0]
inventory = []
mapBoard = '''
▮▮▮▮▮▮▮▮▮▮▮
▮▮▮▮▮ ▮▮▮▮▮
▮▮▮▮▮ ▮▮▮▮▮
▮▮▮▮▮  ▮▮▮▮
▮▮▮    ▮▮▮▮
▮    ▮    ▮
▮    ▮▮   ▮
▮    ▮    ▮
▮▮   ▮  ▮▮▮
▮▮▮▮    ▮▮▮
▮▮▮▮   ▮▮▮▮
▮▮▮▮  ▮▮▮▮▮
▮▮▮  ▮▮▮▮▮▮
▮▮▮▮▮▮▮▮▮▮▮
'''

def area(x1, y1, x2, y2): #Defines a function which takes two coordinate points and selects every point between them.
    areaList = []
    for y in range(y2, y1 - 2, -1):
        for x in range(x1, x2 + 1):
            areaList.append([x, y])
    return areaList

def displayScreen():
    print(area(playerPos[0] - 10, playerPos[1] - 5, playerPos[0] + 10, playerPos[1] + 5))
#    row = []
#    prevY = playerPos[1] + 5
#    for space in area(playerPos[0] - 10, playerPos[1] - 5, playerPos[0] + 10, playerPos[1] + 5):
#        if space[1] != prevY:
#            for i in row:
#                print(i, end='')
#                print()
#                print(row)
#                print(prevY)
#                print(space)
#                row = []
#        if space in map:
#            row.append(blockTypes[map[map.index(space) + 1]])
#        else:
#            row.append(' ')
#        prevY = space[1]

def collision(): #Checks for objects around the player.
    coll_returns = []
    for space in area(playerPos[0] - 1, playerPos[1] - 1, playerPos[0] + 1, playerPos[1] + 1):
        if space in map:
            if blockTypes[map[map.index(space) + 1]] == '▮': #Checks for the direction that blocks are in relative to the player.
                if space == [playerPos[0] - 1, playerPos[1]]:
                    coll_returns.append('a')
                if space == [playerPos[0], playerPos[1] + 1]:
                    coll_returns.append('w')
                if space == [playerPos[0] + 1, playerPos[1]]:
                    coll_returns.append('d')
                if space == [playerPos[0], playerPos[1] - 1]:
                    coll_returns.append('s')
            if blockTypes[map[map.index(space) + 1]] in ['v', '^', '>', '<'] and space == playerPos: #Returns a death if a spike overlaps the player.
                coll_returns.append('dead')
            if blockTypes[map[map.index(space) + 1]] == 'C' and space == playerPos: #If a coin is detected, remove it from the board and add it to the score.
                del map[map.index(space) + 1]
                map.remove(map[space])
                coll_returns.append('coin')
            if blockTypes[map[map.index(space) + 1]] == 'E' and space == playerPos:
                coll_returns.append('enemy')
    return coll_returns

if moveError:
    def move(): #Defines the movement function based on keys pressed, but only if the keyboard is installed.
        keysPressed = []
        for key in ['w', 'a', 's', 'd']:
            if keyboard.is_pressed(key):
                keysPressed.append(key)
        for key in keysPressed:
            if key in collision():
                del keysPressed[keysPressed.index(key)]
            
        if 'w' in keysPressed and 's' in collision():
            velocity[1] = 2
        elif 'w' in collision() and velocity[1] > 0:
            velocity[1] = 0
        if 'a' in keysPressed and velocity[0] > -1:
            velocity[0] -= 0.25
        elif 'a' in collision() and velocity[0] < 0:
            velocity[0] = 0
        elif velocity[0] < 0:
            velocity[0] += 0.25
        if 's' in collision() and velocity[1] < 0:
            velocity[1] = 0
            gravity = 0
        else:
            gravity = 0.25
        if 'd' in keysPressed and velocity[0] < 1:
            velocity[0] += 0.25
        elif 'd' in collision() and velocity[0] > 0:
            velocity[0] = 0
        elif velocity[0] > 0:
            velocity[0] -= 0.25
        if not 's' in collision() and velocity[1] > -1:
            velocity[1] -= gravity
        return [playerPos[0] + int(velocity[0]), playerPos[1] + int(velocity[1])]

def playMap(): #A set of other functions collected to do everything needed to run the platformer part. Also returns values that help with entering combat and viewing other important parts of the game.
    global playerPos
    if keyboard.is_pressed('e') and not keyboard.is_pressed('m'):
        for item in inventory:
            print(item, end=', ')
    elif keyboard.is_pressed('m') and not keyboard.is_pressed('e'):
        print(mapBoard)
    else:
        displayScreen()
        playerPos = move()
    time.sleep(0.25)
        
def choices(inventory): #Every item in the game that can be both picked up and used. Gives the action you can do with the item, and what that action does.
    choiceReturns = []
    if 'sword' in inventory:
        choiceReturns.append('attack', 'use sword', 30)
    return choiceReturns

def combat(enemy): #The combat system for enemies. Takes a specific enemy, lets the user make a choice, does a random action for the enemy, and repeats until someone dies.
    global health
    while True:
        print(health)
        print(inventory)
        print(choices(inventory))
        print(enemies[enemy[0]]) #Displays enemy health
        userAttack = input('What do you want to do?: ')
        while userAttack not in choices(inventory):
            print('Invalid choice. Try again.')
            userAttack = input('What do you want to do?: ')
        enemies[enemy[0]] -= choices(inventory)[choices(inventory).index(userAttack)][1] #This sort of jargon is hard to wrap your head around, but this just subtracts the enemy’s health by the damage of the user’s attack.
        if enemies[enemy[0]] < 0: #If enemy is dead
            print('Congratulations, you defeated the enemy!')
            break
        health -= random.choice[enemies[enemy[1]]] #Subtracts the user’s health by the damage of the enemy’s attack.
        if health < 0:
            print(f'Oh no, you were killed by {enemies[enemy[0]]}!')
            return 'dead'

while moveError: #The loop that starts running the game. Includes a method of restarting the game on death.
    playMap()
    if 'enemy' in collision():
        if 'dead' in combat(random.choice(enemies)):
            if input('Game over. Play again?').lower() == 'no':
                break
            else:
                playerPos = [0, 0]
                health = 100
                inventory = []
    if 'dead' in collision():
        if input('Game over. Play again?').lower() == 'no':
            break
        else:
            playerPos = [0, 0]
            health = 100
            inventory = []