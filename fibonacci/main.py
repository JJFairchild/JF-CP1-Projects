#Jonas Fairchild, fibonacci generator

targetIt = int(input("How many digits of the fibonacci sequence should this program produce?: "))
currentIt = 0
x = 1
y = 1

print(x)

while currentIt < targetIt:
    print(x)
    x = x + y
    y = x - y

    currentIt += 1
