from cs50 import *
from sys import *

if len(sys.argv) != 2:
    print("Usage: python caeasar.py (key)")
    exit(1)

def caesar(msg, key):
    result = ""
    ordAmt = 0
    for c in msg:
        if c.isalpha():
            if c.isupper():
                ordAmt = 65
            else:
                ordAmt = 97
            result += chr((((ord(c) - ordAmt) + int(key)) % 26) + ordAmt)
        else:
            result += str(c)
    return result


print("Message: ", end=""); msg = get_string()
print(caesar(msg, sys.argv[1]))