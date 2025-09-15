import random

print(
"""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 to 100.
""")

uDiff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if uDiff == 'easy':
    attempts = 10
elif uDiff == 'hard':
    attempts = 5
else:
    print("Invalid input. Defaulting to easy mode.")
    attempts = 10

number = random.randint(1, 100)
print(f"You have {attempts} attempts remaining to guess the number.")

while attempts > 0:
    guess = int(input("Make a guess: "))
    
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        attempts -= 1
        if attempts > 0:
            print("Too high.")
            print(f"You have {attempts} attempts remaining to guess the number.")
    else:
        attempts -= 1
        if attempts > 0:
            print("Too low.")
            print(f"You have {attempts} attempts remaining to guess the number.")
    
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The number was {number}.")
    