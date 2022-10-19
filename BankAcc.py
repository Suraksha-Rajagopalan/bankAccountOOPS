import os

customer_info_acc = {}
acc_into_balance = {}

def account_customer():
    first = input("Enter your first name:")
    last = input("Enter your last name:")
    acc_number = int(input("Enter your account number:"))
    balance = int(input("Enter the balance in your account:"))
    if (first+last) not in customer_info_acc:
        print(f"Welcome {first} {last}")
        customer_info_acc[first + last] = acc_number
        acc_into_balance[acc_number] = balance
        return first, last, acc_number, balance
    else:
        if customer_info_acc[first + last] ==acc_number:
            print(f"Welcome {first} {last}")
            return first, last, acc_number, balance
        else:
            return None, None, None, None


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Customer(Person):
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance
    def deposit(self):
        money_to_be_added = int(input("Enter the amount to be deposited: "))
        self.balance += money_to_be_added
        print("Money has successfully been deposited")
    def withdraw(self):
        money_to_be_taken = int(input("Enter the money to be withdrawn: "))
        if (money_to_be_taken + 10000) > self.balance:
            print("This process can't take place")
            print(f"Your balance {self.balance}")
            print("You need to keep a balance of Rupess 10000 in your account")
        else:
            self.balance -= money_to_be_taken
            print("Money has been successfully withdrawn")
            return self.balance

def start():
    while True:
        exit = input("Want to exit(y/n): ").lower()
        if exit == 'y':
            print("Exiting......")
            break
        else:
            a, b, c, d = account_customer()
            os.system('cls')
        if a is None:
            print("your details don't match each other")
        else:
            cus = Person(a, b)
            cus_dw = Customer(c, d)
            ans = input("Do you wnt to deposit or withdraw your money: (d/w)  ")
            if ans == 'w':
                amount_left = cus_dw.withdraw()
                acc_into_balance[c] = amount_left
            elif ans == 'd':
                amount_left = cus_dw.deposit()
                acc_into_balance[c] = amount_left
            else:
                print("Enter valid option")
                print("Try again")
        os.system('cls')
start()
