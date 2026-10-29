# Problem 2 - Modules
# Import a module of your choice and show some operations.

import math
import random
from datetime import date

# math module
print("sqrt(81)      =", math.sqrt(81))
print("pi            =", math.pi)
print("factorial(6)  =", math.factorial(6))
print("ceil(4.2)     =", math.ceil(4.2))
print("floor(4.8)    =", math.floor(4.8))
print("gcd(48, 18)   =", math.gcd(48, 18))
print("pow(2, 10)    =", math.pow(2, 10))
print("log10(1000)   =", math.log10(1000))

# random module (seeded so the output is the same every run)
random.seed(1)
print("random int 1-6     :", random.randint(1, 6))
print("random choice      :", random.choice(["BFS", "DFS", "UCS", "A*"]))

# datetime module
today = date.today()
print("Today is", today, "| year:", today.year)
