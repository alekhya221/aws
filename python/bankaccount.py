class BankAccount:
    def __init__(self,name,mobile_no):
        self.name = name
        self.mobile_no = mobile_no
        self.generate_account_no()
        self.balance = 0
        
    def generate_account_no(self):
        import uuid
        self.account_no = str(uuid.uuid4())
    
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient Funds!")
        else:
            self.balance -= amount
b = BankAccount("alekhya",9044424563)
print(b.name)
print(b.account_no)
print(b.mobile_no)
b.deposit(100)
print(b.balance)
b.deposit(1000)
print(b.balance)
b.withdraw(200)
print(b.balance)