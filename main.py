from random import randint
from accaunt import *

savingAccount = SavingAccount()

while True:
    print("Enter 1 to open an acc")
    print("Enter 2 to acess existing account")
    print("Enter 3 to exit")
    userChoice = int(input(""))
    if userChoice == 1:
        name = input("Enter your name: ")
        initialDeposite = int(input("Enter initialDeposite"))
        savingAccount.createAccount(name, initialDeposite)

    elif userChoice == 2:
        name = input("Enter name: ")
        accountNumber = int(input("Enter accountNumber: "))
        authenticateStatus = savingAccount.authenticate(name, accountNumber)
        if authenticateStatus is True:
            while True:
                print("enter 1 to withdraw")
                print("Enter 2 to deposite")
                print("Enter 3 to displaybalance")
                print("Enter 4 to exit")
                userChoice = int(input(""))
                if userChoice == 1:
                    withdrawAmount = int(input("Enter withdrawAmount : "))
                    savingAccount.withdraw(withdrawAmount)
                elif userChoice == 2:
                    depositeAmount = int(input("Enter depositeAmount : "))
                    savingAccount.deposite(depositeAmount)
                elif userChoice == 3:
                    savingAccount.displaybalance(accountNumber)
                elif userChoice == 4:
                    break


    elif userChoice == 3:
        quit()