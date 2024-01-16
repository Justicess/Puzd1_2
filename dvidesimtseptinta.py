#Task 1

class Number:
    @staticmethod
    def number_factorial(number):
        fact = 1
        for i in range (1, number+1):
            fact = fact * i
        return fact
    @classmethod
    def get_factorial(cls,a):
        return cls.number_factorial(a)
    
print(Number.get_factorial(int(input("Write number:"))))

# Task 2

class Words:
    @staticmethod
    def revers_string(word):
        temp_list = list(word)
        temp_list.reverse()
        return ''.join(temp_list)
    @classmethod
    def get_reversed_word(cls, b):
       return cls.revers_string(b)
    
print(Words.get_reversed_word(input("write word: ")))


# Task 3
class BankAccount:

    total_accounts = 0
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts +=1

    def show_balance(self):
        print(f"account name {self.owner}, balance; {self.balance}")
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts
    @staticmethod
    def validate_amount(amount):
        if amount<0:
            return False
        else:
            return True
        

account1 = BankAccount("a",10000)
account2 = BankAccount("b",20000)
account1.show_balance()
account2.show_balance()
print(BankAccount.get_total_accounts())
print(BankAccount.validate_amount(100))
print(BankAccount.validate_amount(-100))
