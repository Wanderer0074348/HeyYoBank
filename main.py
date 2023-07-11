import sys
sys.path.append( './src/' )
from src.BankServices import BankServices as BankServices
from src.NewAccount import NewAccount as NewAccount
from src.TransactionHistory import TransactionHistory as Trhist
def main():
    choice = int(input('Enter 1 to open a new account or 2 to access an existing account or 3 to delete an existing account : '))
    if choice == 1:
        x = NewAccount('John',25,50000,10000)
        x.open_account()
    elif choice == 2:
        userid = int(input('Enter your user id: '))
        x = BankServices(userid)
        choice = int(input('Enter 1 to deposit, 2 to withdraw, 3 to check balance, 4 to transfer: '))
        if choice == 1:
            amount = int(input('Enter the amount to be deposited: '))
            x.deposit(amount)
            y = Trhist(userid,amount)
            y.update_to_Transaction_history_csv()
        elif choice == 2:
            amount = int(input('Enter the amount to be withdrawn: '))
            x.withdraw(amount)
            y = Trhist(userid,amount)
            y.update_to_Transaction_history_csv()
        elif choice == 3:
            x.check_balance()
        elif choice == 4:
            amount = int(input('Enter the amount to be transferred: '))
            userid = int(input('Enter the user id of the person to whom the amount is to be transferred: '))
            x.transfer(amount,userid)
            y = Trhist(userid,amount)
            y.update_to_Transaction_history_csv()
        else:
            print('Invalid choice')
    elif choice == 3:
        userid = int(input('Enter your user id: '))
        x = BankServices(userid)
        x.RemoveAccount()


main()
