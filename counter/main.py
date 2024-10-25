up = True
i = 0
forever = True

while forever:    
    if i == 20:
        up = False
    elif i == 0:
        up = True
    
    if up == True:
        i += 1
    else:
        i -= 1

    print(i)
    
    if i == 0:
        forever = input("Loop again?: ")
        if forever == "Yes":
            forever = True
        else:
            forever = False