class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, deposit):
        self.account_balance += deposit

    def make_withdrawal(self, withdrawal):
        self.account_balance -= withdrawal


rodney = User("Rodney Bautista", "Rodney@icloud.com")
selena = User("Selena Chheang", "SeleanaC@yahoo.com")
ryan = User("Ryan Bautista", "RyanB@gmail.com")

rodney.make_deposit(100)
rodney.make_deposit(30000)
rodney.make_withdrawal(500)
rodney.make_withdrawal(1000)
rodney.make_deposit(35000)


selena.make_deposit(55000)
selena.make_withdrawal(200)
selena.make_deposit(500)

ryan.make_deposit(1000)
ryan.make_deposit(25000)
ryan.make_withdrawal(3000)
ryan.make_deposit(2000)


print(f'{rodney.name} `s account balance is {rodney.account_balance}. Receipt sent to {rodney.email}')
print(f"{rodney.account_balance}")

print(f'{selena.name} `s account balance is {selena.account_balance}. Receipt sent to {selena.email}' )
print(f"{selena.account_balance}")

print(f'{ryan.name} `s account balance is {ryan.account_balance}. Receipt sent to {ryan.email}')
print(f"{ryan.account_balance}")
