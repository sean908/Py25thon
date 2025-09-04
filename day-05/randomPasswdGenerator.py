import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '@', '^', '_', '=']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters you need in your password? \n"))
nr_symbols = int(input("How many symbols you need in your password? \n"))
nr_numbers = int(input("How many numbers you need in your password? \n"))

raw_ele = []
raw_ele.extend(random.choices(letters, k=nr_letters))
raw_ele.extend(random.choices(symbols, k=nr_symbols))
raw_ele.extend(random.choices(numbers, k=nr_numbers))

random.shuffle(raw_ele)
password = ''.join(raw_ele)
print(password)
