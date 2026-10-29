# Problem 3 - String Operations
# Demonstrate some string operations and string methods.

s = "Artificial Intelligence and Expert System"

# basic operations
print("Length       :", len(s))
print("First char   :", s[0])
print("Last char    :", s[-1])
print("Slice [0:10] :", s[0:10])
print("Reversed     :", s[::-1])
print("Concatenate  :", s + " - CSC 3217")
print("Repeat       :", "AI " * 3)
print("'Expert' in s:", "Expert" in s)

# string methods
print("upper()      :", s.upper())
print("lower()      :", s.lower())
print("title()      :", "hello world".title())
print("replace()    :", s.replace("System", "Systems"))
print("split()      :", s.split())
print("join()       :", "-".join(["A", "I", "E", "S"]))
print("find('and')  :", s.find("and"))
print("count('e')   :", s.count("e"))
print("startswith() :", s.startswith("Artificial"))
print("strip()      :", "   padded   ".strip())
print("isdigit()    :", "2026".isdigit())

# f-string formatting
course = "CSC 3217"
week = 5
print(f"{course} is in week {week}")
