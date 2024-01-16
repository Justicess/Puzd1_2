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