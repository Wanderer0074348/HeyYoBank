import csv
import pandas as pd


def CheckMinBalance(balance):
    if balance < 5000:
        print("Minimum balance should be 5000")
        return False
    else:
        return True


def openAccount(creds: list):
    with open("Accounts.csv", "a+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(creds)
    print("Account created successfully")


def UserCredentials():
    name = input("Enter your full name: ")
    balance = int(input("Enter your balance: "))
    if CheckMinBalance(balance):
        return [UserIDGenerator(), name, balance]
    else:
        print("You will need to add more money to your account. Minimum Balance is 5000")
        UserCredentials()


def ViewBalance(id):
    df = pd.read_csv("Accounts.csv")
    print(df.loc[id-1])


def UserIDGenerator():
    df = pd.read_csv("Accounts.csv")
    return len(df)+1


def UserSearchCredentials():
    id_ = int(input("Enter your id: "))
    account_name = input("Enter your name as registered in account: ")
    return [id_, account_name]


def existingUser():
    new_account = input("Do you want to create a new account? (y/n): ")
    if new_account == "y":
        openAccount(UserCredentials())
    else:
        print("1. View Balance\n2. Add Money")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            ViewBalance(UserSearchCredentials()[0])
        else:
            addMoney()


def addMoney():
    id_ = int(input("Enter your id: "))
    amount = int(input("Enter the amount to be added: "))
    df = pd.read_csv("Accounts.csv")
    df.loc[id_-1, "Balance"] += amount
    df.to_csv("Accounts.csv", index=False)
    print("Money added successfully")


def main():
    existingUser()


main()