# Problem 1 - Single Point Crossover

import random


def crossover(p1, p2, point):
    # swap the genes after the crossover point
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2


p1 = input("Enter parent 1: ")
p2 = input("Enter parent 2: ")

print()
print("Parent 1:", p1)
print("Parent 2:", p2)

# each generation breeds from the children of the previous one
for gen in range(1, 6):
    point = random.randint(1, len(p1) - 1)
    c1, c2 = crossover(p1, p2, point)

    print()
    print("Generation", gen, "- crossover point:", point)
    print("Child 1:", c1)
    print("Child 2:", c2)

    p1 = c1
    p2 = c2
