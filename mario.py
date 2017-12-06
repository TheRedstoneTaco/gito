from cs50 import *

# get user input
while True:
    print("Height: ", end="")
    h = get_int()
    if h >= 0 or h <= 23:
        break
    print("Height must be between 0 and 23, inclusive.")
    
for i in range(h):
    for j in range(h - i - 1):
        print(" ", end="")
    for j in range(i + 2):
        print("#", end="")
    print("")