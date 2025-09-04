import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '@', '^', '_', '=']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters you need in your password? \n"))
nr_symbols = int(input("How many symbols you need in your password? \n"))
nr_numbers = int(input("How many numbers you need in your password? \n"))

raw_ele = []
nl = ns = nn = 0
while nl < nr_letters:
    raw_ele.append(letters[random.randint(0, len(letters) - 1)])
    nl += 1
while ns < nr_symbols:
    raw_ele.append(symbols[random.randint(0, len(symbols) - 1)])
    ns += 1
while nn < nr_numbers:
    raw_ele.append(numbers[random.randint(0, len(numbers) - 1)])
    nn += 1

random.shuffle(raw_ele)
password = ''.join(raw_ele)
print(password)
