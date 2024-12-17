#Jonas Fairchild, Final Project

"""
TO DO:
- Add picking up items
- Make the map
"""

import random
import time
import copy

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

if moveError:
    while True:
        try:
            screenSize = int(int(input("What do you want your screen size to be? (Higher = buggier): ")) / 2)
            while screenSize not in range(5, 16):
                print("Input out of range. Try again.")
                screenSize = int(int(input("What do you want your screen size to be? (range from 10-20): ")) / 2)
            else:
                break
        except:
            print("Invalid input. Try again.")

if moveError:
    tutorial = input('Would you like a quick tutorial? Y/n: ').lower()
    while True:
        if tutorial == 'y':
            print('''
Use WASD to move. Space does not do anything, just press W.
Press W while on a ▯ tile to read signs.
Press E to open the inventory. Press M to open the map.
All bossfights are optional, but without fighting bosses you won't have the equipment to beat the game. Bosses are marked with an E.
Be prepared to enter combat with a smaller creature at random! This will happen every few minutes.
If you see an I on the map, that means an item is there. You should pick it up!
''')
            input('Done reading?: ')
            break
        elif tutorial == 'n':
            break
        else:
            print('Invalid input. Try again.')
            tutorial = input('Would you like a quick tutorial? Y/n: ').lower()


blockTypes = ['▮', '▯', 'v', '^', '>', '<', 'C', 'E', 'I']

# Adjusted Tutorial Map (with right-shifted platforms at y = 8)
map = [[1, 0], 0]

playerPos = [1, 1]
gravity = 0.25
velocity = [0, 0]
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

enemies = [
    # Relatively Easy to Defeat
    ['Shrublike Creature', 25, [['attack', 'Vine Whip', 5], ['defend', 'Root Shield', 5], ['heal', 'Photosynthesize', 8]], 'Small Healing Potion'],
    ['Red-Eyed Rabbit', 30, [['attack', 'Frantic Bite', 8], ['attack', 'Scratch', 5], ['defend', 'Quick Dodge', 4]], 'Small Healing Potion'],
    
    # Slightly Harder
    ['Shark', 50, [['attack', 'Bite', 12], ['attack', 'Tail Whip', 7], ['defend', 'Water Veil', 8]], 'Small Healing Potion'],
    ['Octopus', 55, [['attack', 'Ink Spray', 8], ['attack', 'Tentacle Slap', 10], ['defend', 'Ink Defense', 6]], 'Small Healing Potion'],
    ['Wolf', 60, [['attack', 'Bite', 10], ['attack', 'Howl', 12], ['defend', 'Dodge', 5]], 'Small Healing Potion'],
    ['Skinwalker', 65, [['attack', 'Shape Strike', 12], ['attack', 'Terrifying Form', 10], ['heal', 'Absorb Essence', 12]], 'Small Healing Potion'],
    
    # Moderately Hard
    ['Sentient Cactus', 70, [['attack', 'Spike Shoot', 10], ['defend', 'Hardened Spikes', 10], ['heal', 'Absorb Sunlight', 10]], 'Medium Healing Potion'],
    ['Sandworm', 75, [['attack', 'Burrow Attack', 15], ['defend', 'Sand Veil', 8], ['attack', 'Devour', 20]], 'Medium Healing Potion'],
    ['Waterbender', 80, [['attack', 'Water Blast', 12], ['attack', 'Tidal Strike', 15], ['defend', 'Water Wall', 12], ['heal', 'Aqua Healing', 15]], 'Medium Healing Potion'],
    ['Rock Hurler', 85, [['attack', 'Stone Throw', 15], ['defend', 'Rock Barrier', 12], ['attack', 'Boulder Smash', 18]], 'Medium Healing Potion'],
    
    # Even Harder
    ['Massive Frog', 90, [['attack', 'Tongue Lash', 12], ['attack', 'Body Slam', 18], ['defend', 'Swamp Dodge', 10]], 'Large Healing Potion'],
    ['Mudsucker', 95, [['attack', 'Mud Slap', 14], ['defend', 'Mud Barrier', 12], ['heal', 'Regenerate Slime', 15]], 'Large Healing Potion'],
    
    # Very Hard
    ['Falcon', 100, [['attack', 'Dive Bomb', 15], ['attack', 'Talon Strike', 12], ['defend', 'Soar Away', 10]], 'Large Healing Potion'],
    ['Golem', 110, [['attack', 'Rock Smash', 18], ['defend', 'Stone Armor', 15], ['heal', 'Absorb Earth', 20]], 'Large Healing Potion'],
    
    # Hardest Non-Boss Enemies
    ['Lava Bird', 120, [['attack', 'Fiery Peck', 18], ['attack', 'Wing Flare', 22], ['defend', 'Flame Guard', 15]], 'Elixr of Life'],
    ['Magma Slime', 125, [['attack', 'Lava Splash', 20], ['attack', 'Heat Pulse', 25], ['defend', 'Molten Shell', 18], ['heal', 'Molten Regeneration', 18]], 'Elixr of Life'],
    
    # Minibosses
    ['Grassworm', 120, [['attack', 'Vine Crush', 20], ['defend', 'Leaf Shield', 15], ['heal', 'Regrow', 15]], 'Wooden Shield'],
    ['The Silent One', 130, [['attack', 'Shadow Claw', 22], ['attack', 'Silence Strike', 25], ['defend', 'Shadow Fade', 12]], 'Iron Shield'],
    ['The Sandmaster', 140, [['attack', 'Sandstorm', 28], ['defend', 'Sand Cloak', 15], ['heal', 'Desert Absorption', 25]], 'Steel Shield'],
    ['Skrum', 150, [['attack', 'Tentacle Slam', 30], ['attack', 'Ink Burst', 25], ['defend', 'Abyssal Dodge', 18]], 'Platinum Shield'],
    ['Gust', 135, [['attack', 'Hurricane Strike', 24], ['attack', 'Wind Blade', 20], ['defend', 'Gale Shield', 15], ['heal', 'Whirlwind Regeneration', 20]], 'Platinum Shield'],
    ['Vulcan', 200, [['attack', 'Molten Smash', 35], ['attack', 'Eruption', 40], ['defend', 'Lava Armor', 20], ['heal', 'Core Heat Recovery', 30]]]
]

health = 100 
coins = 0
inventory = []

def area(x1, y1, x2, y2): #Defines a function which takes two coordinate points and selects every point between them.
    areaList = []
    for y in range(y2, y1 - 1, -1):
        for x in range(x1, x2 + 1):
            areaList.append([x, y])
    return areaList

def displayScreen():
    for x in range(100):
        print()
    row = []
    prevY = playerPos[1] + 5
    for space in area(playerPos[0] - screenSize, playerPos[1] - screenSize, playerPos[0] + screenSize, playerPos[1] + screenSize):
        if space[1] != prevY:
            for i in row:
                print(i, end='')
                row = []
            print()
        if space in map and space != playerPos:
            row.append(blockTypes[map[map.index(space) + 1]])
        else:
            row.append(' ')
        if space == playerPos:
            row.append(playerName)
        prevY = space[1]

def collision(): #Checks for objects around the player.
    global coins
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
            if blockTypes[map[map.index(space) + 1]] == 'E' and space == playerPos:
                coll_returns.append('enemy')
                coll_returns.append(map[map.index(space) + 2])
            if blockTypes[map[map.index(space) + 1]] == '▯' and space == playerPos:
                coll_returns.append('sign')
                coll_returns.append(map[map.index(space) + 2])
            if blockTypes[map[map.index(space) + 1]] == 'I' and space == playerPos: #If a coin is detected, remove it from the board and add it to the score.
                inventory.append(map[map.index(space) + 2])
                print()
                print(f"Congratulations, you found a {map[map.index(space) + 2]}!")
                del map[map.index(space) + 1]
                del map[map.index(space)]
                time.sleep(2)
            if blockTypes[map[map.index(space) + 1]] == 'C' and space == playerPos: #If a coin is detected, remove it from the board and add it to the score.
                coins += 1
                print()
                print("Congratulations, you found a coin!")
                del map[map.index(space) + 1]
                del map[map.index(space)]
                time.sleep(2)
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
            
        if 'w' in keysPressed and 's' in collision() and 'sign' not in collision():
            velocity[1] = 2
        elif 'w' in collision() and velocity[1] > 0 and 'sign' not in collision():
            velocity[1] = 0
        elif 'w' in keysPressed and 'sign' in collision():
            print()
            print(collision()[collision().index('sign') + 1])
            input("Done reading?: ")
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

    def playMap(): #A set of other functions collected to do everything needed to run the platformer part.
        global coins
        if keyboard.is_pressed('e') and not keyboard.is_pressed('m'):
            for item in inventory:
                print(item, end=', ')
            input("Done reading?: ")
        elif keyboard.is_pressed('m') and not keyboard.is_pressed('e'):
            print(mapBoard)
            input("Done reading?: ")
        else:
            displayScreen()
        time.sleep(0.25)
        
def choices(): #Every item in the game that can be both picked up and used. Gives the action you can do with the item, and what that action does.
    choiceReturns = []
    # Swords (Attack Items)
    if 'Stone Sword' in inventory:
        choiceReturns.append(['Stone Sword', 'attack', 'You swing the Stone Sword with force!', 10])
    if 'Iron Sword' in inventory:
        choiceReturns.append(['Iron Sword', 'attack', 'You slash with the Iron Sword, dealing significant damage!', 15])
    if 'Shortsword' in inventory:
        choiceReturns.append(['Shortsword', 'attack', 'You quickly stab with the Shortsword, a precise strike!', 12])
    if 'Platinum Sword' in inventory:
        choiceReturns.append(['Platinum Sword', 'attack', 'You swing the Platinum Sword, unleashing devastating power!', 25])

    # Shields (Defend Items)
    if 'Wooden Shield' in inventory:
        choiceReturns.append(['Wooden Shield', 'defend', 'You raise the Wooden Shield, blocking incoming damage.', 5])
    if 'Iron Shield' in inventory:
        choiceReturns.append(['Iron Shield', 'defend', 'You brace with the Iron Shield, significantly reducing harm.', 10])
    if 'Steel Shield' in inventory:
        choiceReturns.append(['Steel Shield', 'defend', 'You fortify yourself with the Steel Shield, absorbing heavy blows.', 15])
    if 'Platinum Shield' in inventory:
        choiceReturns.append(['Platinum Shield', 'defend', 'You wield the Platinum Shield, deflecting most attacks.', 20])

    # Healing Potions (Heal Items)
    if 'Small Healing Potion' in inventory:
        choiceReturns.append(['Small Healing Potion', 'heal', 'You drink a Small Healing Potion, feeling a bit better.', 15])
    if 'Medium Healing Potion' in inventory:
        choiceReturns.append(['Medium Healing Potion', 'heal', 'You drink a Medium Healing Potion, regaining health.', 30])
    if 'Large Healing Potion' in inventory:
        choiceReturns.append(['Large Healing Potion', 'heal', 'You consume a Large Healing Potion, restoring substantial health.', 50])
    if 'Elixir of Life' in inventory:
        choiceReturns.append(['Elixir of Life', 'heal', 'You drink the Elixir of Life, fully revitalizing yourself!', 100])

    return choiceReturns

def erase(enemy):
    global map
    for space in area(enemy[0] - 10, enemy[1] - 10, enemy[0] + 10, enemy[1] + 10):
        if space in map:
            if blockTypes[map[map.index(space) + 1]] == 'E':
                del map[map.index(space) + 1]
                del map[map.index(space)]

def combat(enemy): #The combat system for enemies. Takes a specific enemy, lets the user make a choice, does a random action for the enemy, and repeats until someone dies.
    global health
    tempEnemy = copy.deepcopy(enemies[enemy])
    userImmunity = 0
    enemyImmunity = 0
    print(f"Oh no, you encountered a {tempEnemy[0]}!")
    while True:
        print()
        
        healItems = []
        defItems = []
        attackItems = []
        for item in choices():
            if item[1] == 'heal':
                healItems.append(item[0])
            if item[1] == 'defend':
                defItems.append(item[0])
            if item[1] == 'attack':
                attackItems.append(item[0])
        if attackItems != []:
            print("Attack items:")
        for i in attackItems:
            print(i, end = "\n")
        if defItems != []:
            print("Defense items:")
        for i in defItems:
            print(i, end = "\n")
        if healItems != []:
            print("Healing items:")
        for i in healItems:
            print(i, end = "\n")
        
        print()
        
        print(f"Your health: {health}/100")
        print(f"{tempEnemy[0]} health: {tempEnemy[1]}/{enemies[enemy][1]}") #Displays enemy health

        print()
        
        userAttack = input('What do you want to do?: Use ')
        while userAttack not in inventory:
            print('Invalid choice. Try again.')
            
            print()

            healItems = []
            defItems = []
            attackItems = []
            for item in choices():
                if item[1] == 'heal':
                    healItems.append(item[0])
                if item[1] == 'defend':
                    defItems.append(item[0])
                if item[1] == 'attack':
                    attackItems.append(item[0])
            if attackItems != []:
                print("Attack items:")
            for i in attackItems:
                print(i, end = "\n")
            if defItems != []:
                print("Defense items:")
            for i in defItems:
                print(i, end = "\n")
            if healItems != []:
                print("Healing items:")
            for i in healItems:
                print(i, end = "\n")
        
            print()
        
            print(f"Your health: {health}/100")
            print(f"{tempEnemy[0]} health: {tempEnemy[1]}/{enemies[enemy][1]}") #Displays enemy health
            
            print()
            
            userAttack = input('What do you want to do?: Use ')
        
        for item in choices():
            if item[0] == userAttack:
                print(item[2])
                print()
                if item[1] == 'attack':
                    userImmunity = 0
                    tempEnemy[1] -= (abs(item[3] - enemyImmunity)) #Subtracts the enemy’s health by the damage of the user’s attack.
                elif item[1] == 'defend':
                    userImmunity = item[3]
                elif item[1] == 'heal':
                    userImmunity = 0
                    health += item[3]
                    if health > 100:
                        health = 100
            
        
        if tempEnemy[1] <= 0: #If enemy is dead
            print(f'Congratulations, you defeated the {tempEnemy[0]}!')
            erase(playerPos)
            time.sleep(2)
            try:
                inventory.append(tempEnemy[3])
                return 'survived'
            except:
                return 'survived'
        
        enemyAttack = tempEnemy[2][random.randint(tempEnemy[2].index(tempEnemy[2][0]), tempEnemy[2].index(tempEnemy[2][-1]))] #Subtracts the user’s health by the damage of the enemy’s attack.
        print(f"The {tempEnemy[0]} used {enemyAttack[1]}")
        if enemyAttack[0] == 'attack':
            enemyImmunity = 0
            health -= (abs(enemyAttack[2] - userImmunity))
        elif enemyAttack[0] == 'defend':
            enemyImmunity = enemyAttack[2]
        elif enemyAttack[0] == 'heal':
            enemyImmunity = 0
            tempEnemy[1] += enemyAttack[2]
            if tempEnemy[1] >= enemies[enemy][1]:
                tempEnemy[1] = enemies[enemy][1]


        if health <= 0:
            print(f'Oh no, you were killed by a {tempEnemy[0]}!')
            return 'dead'

def zone():
    if playerPos in area(1, 1, 20, 20):
        return "Rolling Hills"
    elif playerPos in area(11, 21, 30, 50) or playerPos in area(21, 11, 40, 80):
        return "Grassy Plains"
    elif playerPos in area(31, 31, 60, 60):
        return "Dark Forest"
    elif playerPos in area(1, 41, 20, 80) or playerPos in area(-9, 61, 10, 90):
        return "Dune Desert"
    elif playerPos in area(-19, 41, 0, 80):
        return "The Ocean"
    elif playerPos in area(11, 71, 40, 100):
        return "Windy Cliffs"
    elif playerPos in area(61, 51, 70, 80):
        return "Rapids"
    elif playerPos in area(41, 61, 60, 80):
        return "Bog Swamp"
    elif playerPos in area(21, 101, 30, 120):
        return "Mt. Doom"
    else:
        return "Nowhere"
    
def zoneEnemies():
    if "Rolling Hills:" in zone():
        return ""
    elif "Grassy Plains" in zone():
        return random.randint(0, 1)
    elif "Ocean" in zone():
        return random.randint(2, 3)
    elif "Dark Forest" in zone():
        return random.randint(4, 5)
    elif "Dune Desert" in zone():
        return random.randint(6, 7)
    elif "Rapids" in zone():
        return random.randint(8, 9)
    elif "Bog Swamp" in zone():
        return random.randint(10, 11)
    elif "Windy Cliffs" in zone():
        return random.randint(12, 13)
    elif "Mt. Doom" in zone():
        return random.randint(14, 15)
    
prevZone = copy.copy(zone())
while moveError: #The loop that starts running the game. Includes a method of restarting the game on death.
    if prevZone != zone():
        print()
        print(f"Entering new zone! Welcome to: {zone()}!")
        prevZone = copy.copy(zone())
        time.sleep(2)
    move()
    playerPos = move()
    playMap()
    if 'enemy' in collision():
        if 'dead' in combat(collision()[collision().index('enemy') + 1]):
            restartGame = input('Game over. Play again? Y/n: ').lower()
            while True:
                if restartGame == 'n':
                    moveError = False
                    break
                elif restartGame == 'y':
                    playerPos = [1, 1]
                    health = 100
                    inventory = []
                    prevZone = "Rolling Hills"
                    break
                else:
                    print('Invalid input. Try again.')
                    restartGame = input('Game over. Play again? Y/n: ').lower()
    elif random.randint(1, 100) == 1 and zone() not in ["Nowhere", "Rolling Hills"]:
        if 'dead' in combat(zoneEnemies()):
            restartGame = input('Game over. Play again? Y/n: ').lower()
            while True:
                if restartGame == 'n':
                    moveError = False
                    break
                elif restartGame == 'y':
                    playerPos = [1, 1]
                    health = 100
                    inventory = []
                    coins = 0
                    prevZone = "Rolling Hills"
                    break
                else:
                    print('Invalid input. Try again.')
                    restartGame = input('Game over. Play again? Y/n: ').lower()
    if 'dead' in collision():
        restartGame = input('Game over. Play again? Y/n: ').lower()
        while True:
            if restartGame == 'n':
                moveError = False
                break
            elif restartGame == 'y':
                playerPos = [1, 1]
                health = 100
                inventory = []
                prevZone = "Rolling Hills"
                break
            else:
                print('Invalid input. Try again.')
                restartGame = input('Game over. Play again? Y/n: ').lower()