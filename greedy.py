from cs50 import * # you know what this is

# Get user input
while True:
    print("Change: ", end="")
    amount = get_float()
    if amount >= 0:
        break

amount = round(amount * 100) # deal with it this way to prevent imprecision

coins = 0 # Amount of coins
while amount > 0:
    if amount - 25 >= 0:
        amount -= 25
    elif amount - 10 >= 0:
        amount -= 10
    elif amount - 5 >= 0:
        amount -= 5
    elif amount - 1 >= 0:
        amount -= 1
    coins += 1

print(coins) # Give result to the user