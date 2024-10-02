print("This program will calculate the area of squares, rectangles, triangles, circles, and trapezoids.")
shape = input("What shape would you like to calculate?: ")

temp = 0
temp1 = 0
temp2 = 0

if shape == "square":
    temp = float(input("What is the side length of your square?: "))
    print(f"The area of your square is {temp ** 2}.")
elif shape == "rectangle":
    temp = float(input("What is the length of your rectangle?: "))
    temp1 = float(input("What is the width of your rectangle?: "))
    print(f"The area of your rectangle is {temp * temp1}.")
elif shape == "triangle":
    temp = float(input("What is the base of your triangle?: "))
    temp1 = float(input("What is the height of your triangle?: "))
    print(f"The area of your triangle is {(temp * temp1) / 2}.")
elif shape == "circle":
    temp = float(input("What is the radius of your circle?: "))
    print(f"The area of your circle is {3.14159 * temp ** 2}.")
elif shape == "trapezoid":
    temp = float(input("What is the first base of your trapezoid?: "))
    temp1 = float(input("What is the second base of your trapezoid?: "))
    temp2 = float(input("What is the height of your trapezoid?: "))
    print(f"The area of your trapezoid is {((temp + temp1) / 2) * temp2}")
else:
    print("Invalid argument. Check spelling and make sure your input is lowercase.")