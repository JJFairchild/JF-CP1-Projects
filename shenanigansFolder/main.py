def area(x1, y1, x2, y2): #Defines a function which takes two coordinate points and selects every point between them.
    areaList = []
    for y in range(y2, y1 - 2, -1):
        for x in range(x1, x2 + 1):
            areaList.append([x, y])
    return areaList
playerPos = [0, 0]
print(area(playerPos[0] - 10, playerPos[1] - 5, playerPos[0] + 10, playerPos[1] + 5))