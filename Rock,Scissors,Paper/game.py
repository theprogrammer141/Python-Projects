import random

random_number = random.randint(0, 2)
options = ["rock", "scissors", "paper"]
user_wins = 0
computer_wins = 0

while True:
    user_input = str(input("Choose from rock/scissors/paper or enter q to quit: ")).lower()
    #rock: 0, scissors: 1, paper: 2

    computer_choice = options[random_number]
    print("Computer picked: ", computer_choice)

    if user_input == "q":
        break

    if user_input not in options:
        continue

    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        user_wins += 1
        print("\n")

    elif user_input == "paper" and computer_choice == "rock":
        print("You won!")
        user_wins += 1
        print("\n")

    elif user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        user_wins += 1
        print("\n")

    else:
        print("You lost!")
        computer_wins += 1
        print("\n")
        continue

print("User wins: ", user_wins)
print("Computer wins: ", computer_wins)
print("Goodbye!")