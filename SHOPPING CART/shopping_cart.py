foods = []
prices = []
total = 0

while True:
    item = str(input("Enter the item you want to buy or press q to quit): "))
    if item.lower() == "q":
        break
    else:
        price = float(input(f'Enter the price of the {item}: $'))
        foods.append(item)
        prices.append(price)


print("\n")
print("---------YOUR CART----------")
for f, p in zip(foods, prices):
    print(f'{f} : ${p}')

for p in prices:
    total += p

print("-----------------------------")
print(f'Your total is: {total}')
print("-----------------------------")