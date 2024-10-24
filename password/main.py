#Jonas Fairchild, Password Validator

password = input("What would you like your password to be?: ")

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specials = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]


num = False
spec = False
while not len(password) >= 8 or not num or not spec:
    
    if not len(password) >= 8:
        print("Your password is under 8 chracters.")
        password = input("What would you like your password to be?: ")
        continue
    
    num = False
    for number in numbers:
        if number in password:
            num = True
    if num == False:
        print("Your password does not have a number.")
        password = input("What would you like your password to be?: ")
        continue
    
    spec = False
    for special in specials:
        if special in password:
            spec = True
    if spec == False:
        print("Your password does not have a special character.")
        password = input("What would you like your password to be?: ")
        continue

print("Successfully set password!")
    