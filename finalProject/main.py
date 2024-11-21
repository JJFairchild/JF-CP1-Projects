blockTypes = ['▮', 'v', '^', '>', '<', 'C', 'M']
playerPos = [0, 0]
mapBlocks = [playerPos, 3, [-1, -2], 0, [0, -2], 0, [1, -2], 0]
gravity = 1.5
velocity = 0
coins = 0

def area(x1, y1, x2, y2): #Defines a function which takes two coordinate points and selects every point between them.
    areaList = []
    for y in range(y1, y2 + 2):
        for x in range(x1, x2 + 1):
            areaList.append([x, -1 * y])
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
        if space in mapBlocks:  #Adds the space type to the current row.
            mapRow.append(blockTypes[mapBlocks[mapBlocks.index(space) + 1]])
        else:
            mapRow.append(' ')

def collision(): #Checks for objects around the player.
    coll_returns = []
    for space in area(playerPos[0] - 1, playerPos[1] - 1, playerPos[0] + 1, playerPos[1] + 1):
        if space in mapBlocks:
            if blockTypes[mapBlocks[mapBlocks.index(space) + 1]] == '▮': #Checks for the direction that blocks are in relative to the player.
                if space == [playerPos[0] - 1, playerPos[1]]:
                    coll_returns.append('a')
                if space == [playerPos[0], playerPos[1] + 1]:
                    coll_returns.append(' ')
                if space == [playerPos[0] + 1, playerPos[1]]:
                    coll_returns.append('d')
                if space == [playerPos[0], playerPos[1] - 1]:
                    coll_returns.append('s')
            if blockTypes[mapBlocks[mapBlocks.index(space) + 1]] in ['v', '^', '>', '<'] and space == playerPos: #Returns a death if a spike overlaps the player.
                coll_returns.append('dead')
            if blockTypes[mapBlocks[mapBlocks.index(space) + 1]] == 'C' and space == playerPos: #If a coin is detected, remove it from the board and add it to the score.
                del mapBlocks[mapBlocks.index(space) + 1]
                mapBlocks.remove(mapBlocks[space])
                coins += 1
    return coll_returns

def jump():
    #Used in the move function. Adds a certain value to the player's velocity, then uses gravity to take it back down until it hits something. May decide to make part of the move function.
    pass

def move():
    #Uses an advanced method to check if a key is being held down, then accellerates until it reaches top speed. playerPos is a less accurate, rounded version of this number. Also has an option to increase gravity when holding s.
    pass

