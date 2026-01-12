class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

acc = Account("Arun python class", 5000)
acc.deposit(1000)
acc.withdraw(2000)
print(acc.balance)
