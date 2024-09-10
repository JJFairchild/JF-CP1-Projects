def area(x, y):
    a=x*y
    return a

def volume(x, y, z):
   temp = area(x, y)
   v = temp * z
   return v

x = 5
y = 3
paperArea = area(x, y)
print(f"The paper's area is {paperArea} square inches.")

length = 4
width = 6
height = 2
boxVolume = volume(length, width, height)
print(f"The box's volume is {boxVolume} cubic feet.")