class BankAccount:
    account_count=0


    def __init__(self,name,email,balance):
        self.name=name
        self.email=email
        self._balance=balance
        BankAccount.account_count += 1


    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"${amount} deposited successfully.")
        else:
            print("amount should be positive number")

    def withdraw(self,amount):
            if amount<=0:
                print("amount should be greater than zero.")
            elif amount>self._balance:
                print("This amount is greater than your money")
            else:
                self._balance-=amount
                print(f"your money become {self.balance}")

    @property
    def balance (self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value>0:
            self._balance=value
            print("proccess is successful")
        else:
            print("Value should be positive number")
    def display_account(self):

        return (
            f"Name: {self.name}\n"
            f"Email: {self.email}\n"
            f"Balance: ${self.balance:.2f}"
        )

accounts = []


def create_account():
    print("========create account==========")
    name = input("Enter ur name: ")
    email = input("Enter ur email: ")
    balance = float(input("Enter ur initial balance: "))
    account = BankAccount(name, email, balance)
    accounts.append(account)
    print("\n Account Created Successfully ")


def show_accounts():
    if len(accounts) == 0:
        print("\n No Accounts Yet ! \n")
        return
    for account in accounts:
        account.display_account()   


def choose_account():
    if len(accounts) == 0:
        print("\n No Accounts Yet ! \n")
        return

    print(" avilable accs: ")

    for index, account in enumerate(accounts):
        print(f"{index + 1} {account.name}")

    choise = int(input("Choose ur account: "))
    if choise < 1 or choise > len(accounts):
        print("invalid")
        return None

    return accounts[choise - 1]

account1=BankAccount("Hanen","hanenhikal@gmail",1000)
account2=BankAccount("Ali","alimohamed",2000)
print(account1.email)

account2.withdraw(1200)

print(BankAccount.account_count)



