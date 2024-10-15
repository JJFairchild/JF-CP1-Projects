#Jonas Fairchild, What are these numbers?

num = int(input("What number would you like to format?: "))
print("This number as an integer with commas is: {:,}".format(num))
print("This number as a float with 4 decimal places is: {:.4f}".format(num))
print("This number as a percentage is: {:%}".format(num))
print("This number as an amount in dollars is: ${:.2f}".format(num))

