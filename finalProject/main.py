#Jonas Fairchild, Final Project
playerName = input('Select a one-character name for your player: ')
while len(playerName) != 1:
    print('Invalid player name. Try again.')
    playerName = input('Select a one-character name for your player: ')
blockTypes = ['▮', '▯', 'v', '^', '>', '<', 'C', playerName, 'E']
playerPos = [0, 0]
gravity = 0.25
velocity = [0, 0]
coins = 0
import time
map = [playerPos, 7, [-1, -2], 0, [0, -2], 0, [1, -2], 0]
inventory = []

def area(x1, y1, x2, y2): #Defines a function which takes two coordinate points and selects every point between them.
    areaList = []
    for y in range(y1, y2 + 2):
        for x in range(x1, x2 + 1):
            areaList.append([x, y])
    return areaList

def displayScreen(): #Displays the current visible screen.
    mapRow = []
    prevY = playerPos[1] - 5
    for space in area(playerPos[0] - 10, playerPos[1] - 5, playerPos[0] + 10, playerPos[1] + 5): #Checks every square in a certain area around the player.
        if space[1] != prevY: #Checks if the Y value is new, and if so prints the row.
            for block in mapRow:
                print(block, end = '')
            print()
            mapRow = []
        prevY = space[1]
        if space in map:  #Adds the space type to the current row.
            mapRow.append(blockTypes[map[map.index(space) + 1]])
        else:
            mapRow.append(' ')

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

try: #Checks if the keyboard is installed and does not run the rest of the program if not.
    import keyboard
    moveError = True
except:
    print("Please install the keyboard by typing 'pip3 install keyboard' into the terminal before playing.")
    moveError = False
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

def playMap():
    playReturns = []
    if 'enemy' in collision():
        playReturns.append('enemy')
    if keyboard.is_pressed('e') and not keyboard.is_pressed('m'):
        print(inventory)
    elif keyboard.is_pressed('m') and not keyboard.is_pressed('e'):
    
    else:
        displayScreen()
        move()