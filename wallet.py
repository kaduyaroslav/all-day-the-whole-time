class Wallet:
    def __init__(self, user, balance=0,):
        self.user = user
        self.balance = balance
        self.history = []


    def deposit(self, amount):
        if amount <= 0:
            print(f"Error. The sum must be greater than zero.")
            return


        self.balance += amount
        self.history.append(f"+{amount}")
        print(f"{amount} has been deposited. Current balance: {self.balance}")


    def withdraw(self, amount):
        if amount <= 0:
            print("Error. The sum must be greater than zero.")
            return

        if amount > self.balance:
            print("Error: insufficient funds ")
            return

        self.balance -= amount
        self.history.append(f"-{amount}")
        print(f"{amount} has been withdrawn. Current balance: {self.balance}")


    def show(self):
        print(f"{self.user}’s wallet balance: {self.balance}")


    def history_show(self):
        print(f"Transaction history({self.user}):")
        if not self.history:
            print(" Empty for now.")
        for record in self.history:
            print(f"  {record}")



w = Wallet("Иван", 1000)
w.show()
w.deposit(500)
w.withdraw(200)
w.withdraw(5000)
w.history_show()



