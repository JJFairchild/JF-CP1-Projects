houses = 300
housePower = 240

totalPower = houses * housePower
print(f"{totalPower} volts are being used by this neighborhood.")

#In this program, "houses", "housePower", and "totalPower" are all
#objects. Also, 300 and 240 are objects, as well as what is contained
#by print(). Even houses * housePower is an object, since everything
#in Python is an object.

y = 3
x = y
print(issubclass(int, str))