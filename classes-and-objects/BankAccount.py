class BankAccount():
    def __init__(self):
        self.balance = 0
        print("--Welcome to the ATM--")
        self.mainMenu()

    def mainMenu(self):
        while True:
            print("----------------------")
            print("Enter 1 to Deposit Money\nEnter 2 to Withdraw Money\nEnter 3 to Check Balance\nEnter 4 to exit\n")
            choice = int(input("Enter a choice: "))

            if(choice == 1):
                self.checkDeposit()
            elif(choice == 2):
                self.checkWithdraw()
            elif(choice == 3):
                self.checkBalance()
            elif(choice == 4):
                print("Thank you for banking")
                break
            else:
                print("Invalid choice, try again")
            

    def checkDeposit(self):
        try:
            depositAmount = float(input("Enter the amount to be deposited: "))

            if(depositAmount <= 0):
                print("Please enter a positive value ")
            else:   
                self.balance += depositAmount
                print(f'{'Amount deposited: LKR '}{depositAmount}')
        except ValueError:
            print("Error, please enter a numeric value")

    def checkWithdraw(self):
        try:
            withdrawAmount = float(input("Enter an amount to Withdraw: "))
            if(withdrawAmount <= 0):
                print("Withdraw amount must be positive")
            elif(withdrawAmount > self.balance):
                print("Not enough funds")
            else:
                self.balance -= withdrawAmount
                print(f'{"Withdrawed : LKR "}{withdrawAmount}')
        except ValueError:
            print("Error, please enter a numeric value")

    def checkBalance(self):
        try:
            print(f'{"Available balance: LKR "}{self.balance}')

        except ValueError:
            print("Error, please enter a numeric value")


