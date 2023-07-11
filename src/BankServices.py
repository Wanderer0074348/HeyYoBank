import pandas as pd

class BankServices():
    def __init__(self,userid:int)->None:
        self.userid = userid
    def deposit(self,amount:int)->None:
        df = pd.read_csv('./files/OpenedAccounts.csv')
        df.loc[df['Id']==self.userid,'Deposit'] += amount
        df.to_csv('./files/Accounts.csv',index=False)
        print('Amount deposited successfully')
    def withdraw(self,amount:int)->None:
        df = pd.read_csv('./files/OpenedAccounts.csv')
        df.loc[df['Id']==self.userid,'Deposit'] -= amount
        df.to_csv('./files/Accounts.csv',index=False)
        print('Amount withdrawn successfully')
    def check_balance(self)->None:
        df = pd.read_csv('./files/OpenedAccounts.csv')
        print('Your current balance is: ',df.loc[df['Id']==self.userid,'Deposit'].values[0])
    def transfer(self,amount:int,userid:int)->None:
        df = pd.read_csv('./files/OpenedAccounts.csv')
        df.loc[df['Id']==userid,'Deposit'] += amount
        df.loc[df['Id']==self.userid,'Deposit'] -= amount
        df.to_csv('./files/OpenedAccounts.csv',index=False)
        print('Amount transferred successfully')
    def RemoveAccount(self)->None:
        df = pd.read_csv('./files/OpenedAccounts.csv')
        df = df[df['Id']!=self.userid]
        df.to_csv('./files/OpenedAccounts.csv',index=False)
        print('Account removed successfully')

