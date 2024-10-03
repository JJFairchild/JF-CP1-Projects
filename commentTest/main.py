class BankAccount: #Puts the following functions into a class so they are grouped together.
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #Defines a funtion that takes in an amount greater than 0 and adds it to what is already contained in 'self'.
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): #Defines a function that takes in an amount between 0 and what is already contained in 'self', then subtracts the amount from it.
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self): #Defines a function to return the balance of a specified account.
        return self.balance

def create_account(): #Defines a function that creates an account by requesting an account number to make it for, then creating the account under that number. It also requests and makes an initial balance.
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main(): #Defines a function 'main' that requests an input then acts accordingly. More detail for individual actions.
    accounts = {} #Sets 'accounts' to an an empty list.
    while True: #A forever loop
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") #Asks the user what action they would like to do.
        
        if choice == '1': #Performs the actions needed to create an account, then adds it to 'accounts'.
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: #Inputs a specific account number, then uses it to perform one of the other available actions that use account numbers.
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2': #Adds a requested deposit to the requested account
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3': #Withdrawls the requested amount from the specified account
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") #Prints the current balance of the requested account.
            else:
                print("Account not found.") #Standard error message.
        
        elif choice == '5': #Exits the program if user chooses 5.
            print("Thank you for using our banking system. Goodbye!")
            break #I think this is what stops the program.
        
        else:
            print("Invalid choice. Please try again.") #Prints if original number is not in range 1-5.

if __name__ == "__main__": #Runs the program again.
    main()