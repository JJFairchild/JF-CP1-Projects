#Jonas Fairchild, what is my grade

grade = int(input("What is your grade? (no %): "))

if grade <= 60:
    print("You have an F.")
elif grade <= 63:
    print("You have a D-.")
elif grade <= 67:
    print("You have a D.")
elif grade <= 70:
    print("You have a D+.")
elif grade <= 73:
    print("You have a C-.")
elif grade <= 77:
    print("You have a C.")
elif grade <= 80:
    print("You have a C+.")
elif grade <= 83:
    print("You have a B-.")
elif grade <= 87:
    print("You have a B.")
elif grade <= 90:
    print("You have a B+.")
elif grade <= 93:
    print("You have an A-.")
elif grade <= 97:
    print("You have an A.")
elif grade <= 100:
    print("You have an A+.")
else:
    print("There was an error.")