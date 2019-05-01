
class Account:
        def __init__(self,owner,balance):
            self.owner = owner
            self.balance = balance

        def __repr__(self):
            return f"Owner: {self.owner}, Balance: {self.balance} "
acct1 = Account('Jose',100)
print(acct1)
