#Jonas Fairchild Personal Information Converter

print("This program will make you a personal identification card.")
name = input("Type your full name.: ")
age = input("Type your age.: ")
height = input("Type your height in centimeters.: ")
num = input("What is your favorite number?: ")

print(f"""Original input information:

Name = {name}
Age = {age}
Height = {height}
Favorite number: {num}
""")



print(f"""
Completed information card:
      
      
User Name: {str(name)}

User information:

Age: {int(age)} years
Height (cm): {int(height)}

FaVoRiTe NuMbEr!1!!!: {str(num)}!!1!

""")