class BankAccount:
    name="consolidated bank"
    def __init__(self,banking,withdraw):
        self.banking=banking
        self.withdraw=withdraw
    def newest_account(self):
        return f"I will deposit sh.{self.banking} today"
    def parent_account(self):
        return f"I will withdraw sh{self.withdraw} to pay my employee"