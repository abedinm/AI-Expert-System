# Problem 7 - Tuples & Sets
# Examples following the official Python tutorial (docs.python.org, section 5.3 and 5.4).

# ---------- Tuples: ordered and immutable ----------
t = 12345, 54321, "hello!"     # tuple packing (parentheses are optional)
print("Tuple:", t)
print("t[0]:", t[0])

nested = t, (1, 2, 3, 4, 5)    # tuples can be nested
print("Nested:", nested)

# tuples cannot be changed: t[0] = 888 would raise a TypeError
empty = ()
singleton = ("hello",)         # note the trailing comma
print("len(empty) =", len(empty), "| len(singleton) =", len(singleton))

x, y, z = t                    # sequence unpacking
print("Unpacked:", x, y, z)

point = (3, 4)
print("Count of 3:", point.count(3), "| index of 4:", point.index(4))

# ---------- Sets: unordered, no duplicates ----------
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print("Set (duplicates removed):", sorted(basket))
print("'orange' in basket:", "orange" in basket)
print("'crabgrass' in basket:", "crabgrass" in basket)

a = set("abracadabra")
b = set("alacazam")
print("a      :", sorted(a))
print("b      :", sorted(b))
print("a - b  :", sorted(a - b))   # in a but not in b
print("a | b  :", sorted(a | b))   # in a or b or both
print("a & b  :", sorted(a & b))   # in both a and b
print("a ^ b  :", sorted(a ^ b))   # in a or b but not both

basket.add("mango")
basket.discard("pear")
print("After add/discard:", sorted(basket))

# set comprehension
letters = {ch for ch in "abracadabra" if ch not in "abc"}
print("Set comprehension:", sorted(letters))
