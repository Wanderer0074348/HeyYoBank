import pandas as pd

class NewAccount:
    def __init__(self,name:str,age:int,income:int,deposit:int)->None:
        self.name = name
        self.age = age
        self.income = income
        self.deposit = deposit
    def open_account(self)->None:
        df = pd.DataFrame({'Id':self.UserIDGenerator(),'Name':[self.name],'Age':[self.age],'Income':[self.income],'Deposit':[self.deposit]})
        df.to_csv('./files/OpenedAccounts.csv',mode='a',header=False,index=False)
        print('Account opened successfully')
    def UserIDGenerator(self):
        df = pd.read_csv("files/Accounts.csv")
        return len(df)+1

