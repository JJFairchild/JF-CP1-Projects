num = int(input("What number do you want multiples of?: "))

start = "   0 | "
multiply = ""
for i in range(1, num + 1):
    start += (str(i) +  " | ")
    for j in range(0, 13):
        multiply = (i)