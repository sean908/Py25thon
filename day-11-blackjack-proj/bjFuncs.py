def juggWentOver(cardsList):
    if sum(cardsList) > 21:
        return True
    return False

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def compare_scores(player_score, comp_score):
    if player_score > 21:
        return "You went over. You lose!"
    elif comp_score > 21:
        return "Computer went over. You win!"
    elif player_score == comp_score:
        return "It's a draw!"
    elif player_score > comp_score:
        return "You win!"
    else:
        return "You lose!"

def is_blackjack(cards):
    return len(cards) == 2 and calculate_score(cards) == 21
    