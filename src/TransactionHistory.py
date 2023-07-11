import pandas as pd
import os
class TransactionHistory:
    def __init__(self,Userid,TransactionMade:int):
        self.Userid = Userid
        self.TransactionMade = TransactionMade
    def update_to_Transaction_history_csv(self):
        if os.path.exists(f'./TransactionFiles/{self.Userid}.csv'):
            df = pd.DataFrame({'TransactionMade':[self.TransactionMade]})
            df.to_csv(f'./TransactionFiles/{self.Userid}.csv',mode='a',header=False,index=False)
        else:
            with open(f'./TransactionFiles/{self.Userid}.csv','w') as f:
                f.write(f'TransactionMade of {self.TransactionMade}')
