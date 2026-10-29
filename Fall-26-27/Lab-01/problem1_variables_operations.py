# Problem 1 - Variables & Operations
# Assign values to some variables, perform different operations and print the results.

a = 17
b = 5
name = "AIES"
price = 12.5
is_open = True

print("Types:", type(a), type(price), type(name), type(is_open))

# arithmetic operations
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)     # true division -> float
print("a // b =", a // b)    # floor division -> int
print("a % b  =", a % b)     # remainder
print("a ** b =", a ** b)    # power

# comparison and logical operations
print("a > b       :", a > b)
print("a == 17     :", a == 17)
print("a > 10 and b > 10 :", a > 10 and b > 10)
print("a > 10 or b > 10  :", a > 10 or b > 10)
print("not is_open :", not is_open)

# mixing types
total = price * b
print("price * b =", total)
print("Course: " + name + ", total = " + str(total))

# a variable's type can change when a new value is assigned
a = "now a string"
print("a is now", type(a))
