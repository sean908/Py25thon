import random
import bjFuncs
import os

def play_blackjack():
    os.system('clear' if os.name == 'posix' else 'cls')
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    comp_cards = []
    
    print(r"""
    ______ _            _    _            _    
    | ___ \ |          | |  (_)          | |   
    | |_/ / | __ _  ___| | ___  __ _  ___| | __
    | ___ \ |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_/ / | (_| | (__|   <| | (_| | (__|   < 
    \____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                           _/ |                
                          |__/                 
    """)
    
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    comp_cards.append(random.choice(cards))
    
    game_over = False
    
    while not game_over:
        player_score = bjFuncs.calculate_score(player_cards)
        comp_score = bjFuncs.calculate_score(comp_cards)
        
        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {comp_cards[0]}")
        
        if bjFuncs.is_blackjack(player_cards) or bjFuncs.is_blackjack(comp_cards) or player_score > 21:
            game_over = True
        else:
            user_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_continue == 'y':
                player_cards.append(random.choice(cards))
            else:
                game_over = True
    
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(random.choice(cards))
        comp_score = bjFuncs.calculate_score(comp_cards)
    
    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(bjFuncs.compare_scores(player_score, comp_score))

while True:
    want_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_play == 'y':
        play_blackjack()
    else:
        break