blockTypes = ['▮', '▯', 'v', '^', '>', '<', 'C', 'P', 'E']
playerPos = [0, 0]
map = [playerPos, 7, [-1, -2], 0, [0, -2], 0, [1, -2], 0]
import time

def area(x1, y1, x2, y2): #Defines a function which takes two coordinate points and selects every point between them.
    areaList = []
    for y in range(y2, y1 - 1, -1):
        for x in range(x1, x2 + 1):
            areaList.append([x, y])
    return areaList

def displayScreen():
    row = []
    prevY = playerPos[1] + 5
    for space in area(playerPos[0] - 10, playerPos[1] - 5, playerPos[0] + 10, playerPos[1] + 5):
        if space[1] != prevY:
            for i in row:
                print(i, end='')
                row = []
            print()
        if space in map:
            row.append(blockTypes[map[map.index(space) + 1]])
        else:
            row.append(' ')
        prevY = space[1]

while True:
    displayScreen()
    time.sleep(0.25)