from abc import ABCMeta, abstractmethod
from random import randint


class Account:
    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposite(self):
        return 0

    @abstractmethod
    def displaybalance(self):
        return 0


class SavingAccount(Account):
    def __init__(self):
        self.savingAccounts = {"11111": ["hemil", 1]}

    def createAccount(self, name, initialDeposite):
        self.accountNumber = randint(10000, 99999)
        self.savingAccounts[self.accountNumber] = [name, initialDeposite]
        print("Your account is successfully created, Your account number is {}".format(self.accountNumber))

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Successful!")
                self.accountNumber = accountNumber
            return True
        else:
            print("all keys >>>>>>>>>>>>>" + str(self.savingAccounts.keys()))
            print("name you enter>>>>>>>>>" + name)
            print("name in database>>>>>>>" + self.savingAccounts[accountNumber][0])
            print("Authentication failed")
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawAmount
            print("Withdraw Successful")
            self.displaybalance(self.accountNumber)

    def deposite(self, depositeAmount):
        self.savingAccounts[self.accountNumber][1] += depositeAmount
        print("deposite Successful")
        self.displaybalance(self.accountNumber)

    def displaybalance(self, accountNumber):
        print("Available balance: {}".format(self.savingAccounts[accountNumber][1]))