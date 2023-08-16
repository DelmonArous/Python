class Account:
    def __init__(self, name, account_number, initial_amount, transactions=0):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.count = transactions
    
    def deposit(self, amount):
        self.balance += amount
        self.count += 1
    
    def withdraw(self, amount):
        self.balance -= amount
        self.count += 1
        
    def balance(self):
        return self.balance
   
    def dump(self):
        s = '%s, %s, balance: %s, transactions: %s' % \
            (self.name, self.no, self.balance, self.count)
        print s

a1 = Account('John Olsson', '19371554951', 20000)
a2 = Account('Liz Olsson', '19371564761', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
a1.dump()
a2.dump()

