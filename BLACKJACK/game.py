from art import logo
import random

print(logo)

#Ask the player if they want to play blackjack
shall_continue = True

while shall_continue:
    start = str(input("Do you want to play a 'blackjack' game? Press 'y' to start or 'n' to exit: "))

    if start == 'y':
        deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player_deck = []
        player_score = 0
        computer_deck = []
        computer_score = 0
        random_player_card = random.choice(deck_of_cards)
        random_computer_card = random.choice(deck_of_cards)

        for i in range(0, 2):
            player_deck.append(random_player_card)

        computer_deck.append(random_computer_card)
        player_score = sum(player_deck)
        computer_score = sum(computer_deck)

        print(f"Your cards: {player_deck}, total score = {player_score}")
        print(f"Computer's cards: {computer_deck}, total score = {computer_score}")

        flag = True

        while flag:
            if not player_deck and computer_deck:
                print(f"Your final hand: {player_deck}, total score: {player_score}")
                print(f"Computer's final hand: {computer_deck}, total score: {computer_score}")
                flag = False
                SystemExit

            hit_or_pass = str(input("Press 'y' to take another hit or 'n' to pass: "))
            if hit_or_pass == 'y':
                player_deck.append(random_player_card)
                computer_deck.append(random_computer_card)
                player_score = sum(player_deck)
                computer_score = sum(computer_deck)
                print(f"Your cards: {player_deck}, total score = {player_score}")
                print(f"Computer's cards: {computer_deck}, total score = {computer_score}")
                flag = True
            elif hit_or_pass == 'n':
                computer_deck.append(random_computer_card)
                computer_score = sum(computer_deck)
                print(f"Your final hand: {player_deck}, total score: {player_score}")
                print(f"Computer's final hand: {computer_deck}, total score: {computer_score}")
                flag = False

        if player_score < computer_score:
            print("You lose!")
        elif computer_score == 21:
            print("You lose!")
        elif player_score == 21 and computer_score == 21:
            print("That's a draw!")
        elif player_score == computer_score:
            print("That's a draw!")
        else:
            print("You win!")

    elif start == 'n':
        shall_continue = False
        SystemExit
