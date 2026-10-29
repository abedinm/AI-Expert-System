# Problem 2 - Even Numbers Generator (Lists & Ranges)
# Generate all even numbers from 0 to 100 with a for loop and range(start, stop, step),
# store them in a list and print the list in reverse order.

even_numbers = []
for n in range(0, 101, 2):     # stop is 101 so that 100 is included
    even_numbers.append(n)

print("Even numbers:", even_numbers)
print("Count:", len(even_numbers))

# reverse order using slicing
print("Reversed (slicing):", even_numbers[::-1])

# reverse order using a built-in function
print("Reversed (reversed()):", list(reversed(even_numbers)))
