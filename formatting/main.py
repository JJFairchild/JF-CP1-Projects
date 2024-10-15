#Jonas Fairchild, What are these numbers?

num = int(input("What number would you like to format?: "))
print("This number as an integer with commas is: {:,}".format(num))
print(f"This number as a float with 4 decimal places is: {num/10000}") #Note: This only works if your number is at least 4 digits long and doesn't end in a 0.
print("This number as a percentage is: {:%}".format(num))
print(f"This number as an amount in dollars is: {"$" + str(num/100)}")

