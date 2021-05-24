
class BankAcc:
    name="Equity"
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
        self.balance=0
        
    def show_balance(self):
        return f"Hello{self.name}you balance is{self.balance}"
    def deposit(self,amount):
        self.balance+=amount
        return self.show_balance()

    def withdraw(self,amount):
        if amount>self.balance:
            return f"you can't withdraw {amount}it is below minimum"
          
        else:
             self.balance-=amount
             return self.show_balance()
           
       
    def update_deposit(self,amount):
        if amount>0:  
            self.balance+=amount
            return f"Hello your new balance is {self.show_balance}" 
        else:
            return f"you cannot deposit{amount} it is beyound minimum"
       
    def borrow(self,amount):
        self.loan=0
        self.loan+=amount
        return f"Hello your loan balance is{self.loan}" 

    def repay(self,amount):
        self.loan-=amount
        return f"Hello have repayed{amount}"


    

