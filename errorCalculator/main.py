num1 = 0
while type(num1) != float:
    try:
        num1 = float(input("What is your first number?: "))
    except:
        print("That's not a valid input. Try again.")

num2 = 0
while type(num2) != float:
    try:
        num2 = float(input("What is your second number?: "))
    except:
        print("That's not a valid input. Try again.")

op = 8.0
optry = False
while optry != True:
    print("""1 = +
2 = -
3 = *
4 = **
5 = /
6 = //
7 = %""")
    try:
        op = (input("What operation do you want to perform?: "))
        if int(op) not in range(1, 8):
            print("That's not a valid input. Try again.")
        else:
            if op == "5" and num2 == 0:
                print("You can't divide by 0. Try again.")
            else:
                op = int(op)
                break
    except:
        print("That's not a valid input. Try again.")

if op == 1:
    print(f"Your answer is {num1 + num2}.")
else:
    if op == 2:
        print(f"Your answer is {num1 - num2}.")
    else:
        if op == 3:
            print(f"Your answer is {num1 * num2}.")
        else:
            if op == 4:
                print(f"Your answer is {num1 ** num2}.")
            else:
                if op == 5:
                    print(f"Your answer is {num1 / num2}.")
                else:
                    if op == 6:
                        print(f"Your answer is {num1 // num2}.")
                    else:
                        print(f"Your answer is {num1 % num2}.")