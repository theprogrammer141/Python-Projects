#Generate a random number
#Track the number of times it takes the user to guess the number

import random

random_number = random.randint(1, 10)

print("\n")
print("-" * 30)
print("Hello and welcome to the game!")
print("You will input a random number\nAnd the program will check if you guessed the number right or not\nAnd at the end, the program will output your attempts")
print("-" * 30)

print("\nLet\'s Start!")
print("-" * 30)

number_to_be_guessed = 0
attempts = 0
while number_to_be_guessed != random_number:
    number_to_be_guessed = int(input("Please input a random number: "))

    if number_to_be_guessed == random_number:
        print("Correct!")
        print("-" * 30)
        break
    else:
        print("Keep guessing!")
        attempts += 1


print("Your attempts: ", attempts)
print("-" * 30)