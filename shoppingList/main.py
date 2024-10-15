shopping_list = []
while True:

    action = input("""What would you like to do?

    Enter 1 to add item

    Enter 2 to remove item
                   
    Enter 3 to view the list

    Enter 4 to leave the list:\n""")

    if action =="1":
        item = input("What item would you like to add?: ")
        shopping_list.append(item)
    elif action =="2":
        item = input("What item would you like to remove?: ")
        shopping_list.remove(item)
    elif action =="3":
       print(shopping_list)
    else:
        print("Have a nice day!")
        break