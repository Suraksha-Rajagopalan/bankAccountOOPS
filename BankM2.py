class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Client(Person):
    def __init__(self, first_name, last_name, account_name, balance = 0):
        super().__init__(self, first_name, last_name)
        self.account_name = account_name
        self.balance = balance
    def __str__(self):
        return f'Client: {self.first_name} {self.last_name}\nAccount Balance {self.account_name}: Rs{self.balance}'
    def deposit(self, amount_deposit):
        self.balance += amount_deposit
        print('Deposit accepted')
    def withdrawn(self, amount_withdraw):
        if amount_withdraw >= self.balance:
            print("Money can't be withdrawn")
        else:
            self.balance -= amount_withdraw
            print("Money withdrawn")

def create_client():
    first_name_ct = input("Enter your first name: ")
    last_name_ct = input("Enter your last name: ")
    account_number = input("Enter the account number: ")
    client_1 = Client(first_name_ct, last_name_ct, account_number)
    return client_1

def start():
    my_customer = create_client()
    print(my_customer)
    option = 0

    while option!='E':
        print("Choose: Deposit(d) or withdraw(w) or exit (E): ")
        option = input()

        if option == 'd':
            dep_amount = int(input("Enter the amount to be deposited :"))
            my_customer.deposit(dep_amount)
        elif option == 'w':
            wit_amount = int(input("Enter the amount to be withdrawn: "))
            my_customer.withdrawn(wit_amount)

        print(my_customer)

start()
