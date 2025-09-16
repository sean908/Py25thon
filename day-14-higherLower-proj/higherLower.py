# -*- coding: utf-8 -*-
import random
import os
from art import logo, vs
from data import data

def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_items():
    """Get two random items from data"""
    return random.sample(data, 2)

def display_item(item):
    """Display an item with its description"""
    print(f"{item['name']}, a {item['description']}")

def play_game():
    """Main game logic"""
    clear_screen()
    print(logo)
    
    score = 0
    game_should_continue = True
    
    # Get first two items
    item_a, item_b = get_random_items()
    
    while game_should_continue:
        # Display item A
        print(f"Compare A: ", end="")
        display_item(item_a)
        
        print(vs)
        
        print(f"Against B: ", end="")
        display_item(item_b)
        
        # Get user guess
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        # Check if user is correct
        if (guess == 'A' and item_a['value'] > item_b['value']) or \
           (guess == 'B' and item_b['value'] > item_a['value']):
            score += 1
            clear_screen()
            print(logo)
            print(f"You're right! Current score: {score}")
            
            # Make item B the new item A for next round
            item_a = item_b
            # Get a new item B (make sure it's different from current item A)
            remaining_items = [item for item in data if item != item_a]
            item_b = random.choice(remaining_items)
            
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

def main():
    """Main function to run the game"""
    play_again = True
    
    while play_again:
        play_game()
        
        restart = input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
        if restart != 'y':
            play_again = False
            print("Thanks for playing!")

if __name__ == "__main__":
    main()