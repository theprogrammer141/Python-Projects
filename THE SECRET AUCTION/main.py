from art import logo


print(logo)

final_bidders = {}
max_bid = 0
winner = ""

def add_bidders():
    name = str(input("What is your name? "))
    bid_amount = int(input("Enter your bid: $"))
    final_bidders[name] = bid_amount

print("Welcome to the auction!")
add_bidders()


while True:
    other_bidders = str(input("Are there any other bidders?(yes or no): "))
    if other_bidders == "yes":
        add_bidders()
    elif other_bidders == "no":
        for name, bid in final_bidders.items():
            if bid > max_bid:
                max_bid = bid
                winner = name
        break

print(f'The winner is {winner} with a bid of ${max_bid}')

