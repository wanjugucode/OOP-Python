from datetime import datetime
class BankAcc:
    name="Equity"


    def __init__(self,name,phone_number,loan):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        self.loan=loan
        self.statement=[]
     

    def show_balance(self):
        return f"Hello{self.name}you balance is{self.balance}"

    def withdraw(self,amount):
        if amount>self.balance:
            return f"you can't withdraw {amount}it is below minimum"

        else:
             self.balance-=amount
             return self.show_balance()


    def deposit(self,amount):
        if amount<0:  
            return f"you cannot deposit ksh:{amount} it is below minimum" 
        else:
            self.balance+=amount
            now=datetime.now()
            transaction={
                "amount":50,
                "time":now,
                "narration":"you deposited"}
            self.statement.append(transaction)
            return self.statement
    
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")
        return
    def withdraw(self,amount):
        if amount>self.balance:
            return f"Your balance is {self.balance} and You cant't withdrwaw  {amount} it is below minimum"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={
                "amount":70,
                "time":now,
                "narration":"You withdrew"
            }
            self.statement.append(transaction)
            return self.showbalance()
  
    def show_statement(self):
        for transaction in self.statement:
            amount=transaction["amount"]
            narration=transaction["narration"]
            time=transaction["time"]
            date=time.strftime("%d/%m/%y")
            print(f"{date}:{narration} {amount}")
        return

    def borrow(self,amount):
        self.loan=0
        self.loan+=amount
        return f"Hello your loan balance is{self.loan}" 

    def repay(self,amount):
        self.loan-=amount
        return f"Hello have repayed{amount}"

    

