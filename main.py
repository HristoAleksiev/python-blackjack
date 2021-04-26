############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# from replit import clear
from art import logo
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


final_results = {
    "PlayerOver": "You went Over, you Lose! :(",
    "ComputerOver": "Computer went Over, you Win! :)",
    "BlackDraw": "It's a Draw of Blackjacks! :)",
    "CompBlack": "Computer has a Blackjack, you Lose! :(",
    "PlayerBlack": "You have a Blackjack, you Win, that is Great! :))",
    "PlayerWin": "You have a higher result, you Win! :)",
    "ComputerWin": "The computer has a higher result, you Lose! :(",
    "Draw": "It's a Draw :|",
}

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
computer_hand = []
game_state = "y"
card_draw = ""


def deal_card():
    return random.choice(cards)


def sum_score(hand):
    total = 0
    for card in hand:
        total += card
    return total


def reset_game():
    global player_hand
    global computer_hand 
    global game_state 
    global card_draw 

    player_hand = []
    computer_hand = []
    game_state = "y"
    card_draw = ""


def print_score(player_hand, computer_hand,result_message):
    print(f"Your final hand: {player_hand}, final score: {sum_score(player_hand)}")
    print(f"Computer's final hand: {computer_hand}, final score: {sum_score(computer_hand)}")
    print(final_results[result_message])


def game_mechanics(player_score, computer_score):   
    global card_draw
    if player_score > 21:
        print_score(player_hand, computer_hand, "PlayerOver")
        return
    elif computer_score > 21:
        print_score(player_hand, computer_hand,"ComputerOver")
        return
    elif computer_score == player_score and computer_score == 21:
        print_score(player_hand, computer_hand,"BlackDraw")
        return
    elif computer_score == 21:
        print_score(player_hand, computer_hand,"CompBlack") 
        return   
    elif player_score == 21:
        print_score(player_hand, computer_hand,"PlayerBlack") 
        return
    elif card_draw == "n":
        if player_score > computer_score:
            print_score(player_hand, computer_hand,"PlayerWin")
            return
        elif player_score < computer_score:
            print_score(player_hand, computer_hand,"ComputerWin")
            return
        else:
            print_score(player_hand, computer_hand,"Draw")
            return
    else:
        print(f"Your cards: {player_hand}, current score: {sum_score(player_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")

    card_draw = input("Type 'y' to get another card, type 'n' to pass: ")
    if card_draw == "y":
        player_hand.append(deal_card())
        player_score = sum_score(player_hand)
        
        if computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = sum_score(computer_hand)
            
        game_mechanics(player_score, computer_score)        
    else:
        while computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = sum_score(computer_hand)
        game_mechanics(player_score, computer_score)


def core_game_loop():
    
    reset_game()
    game_state = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    
    if game_state == "y":
        clear()
        print(logo)
    elif game_state == "n":
        return

    player_hand.append(deal_card())
    player_hand.append(deal_card())

    computer_hand.append(deal_card())
    computer_hand.append(deal_card())

    player_score = sum_score(player_hand)
    computer_score = sum_score(computer_hand)

    game_mechanics(player_score, computer_score)

    core_game_loop()


core_game_loop()

# This is a test comment in the file





















