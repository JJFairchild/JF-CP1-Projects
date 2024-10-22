#Jonas Fairchild, Authorized

users = ["Maria", "Jack", "Caleb", "Jonas", "Zoe", "Zack", "Andrew", "Luke"]
admins = ["Jonas"]

user = input("Type your username.: ")

if user in users:
    if user in admins:
        print(f"Hello, {user}. You have admin status.")
    else:
        print(f"Hello, {user}. You have user status.")
else:
    print(f" {user} You are not a registered user. Contact support for more info.")