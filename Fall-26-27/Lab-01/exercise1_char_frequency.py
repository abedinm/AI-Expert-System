# Lab Activity 1 - Exercise 1: Character frequency
# Count how many times each character appears in the input string.
# Example: hello world -> 'h': 1 'e': 1 'l': 3 'o': 2 ' ': 1 'w': 1 'r': 1 'd': 1

text = input("Enter a string: ")

freq = {}
for ch in text:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

# a dictionary keeps insertion order, so characters print in the order they first appear
parts = []
for ch, count in freq.items():
    parts.append(f"'{ch}': {count}")

print("Output:", " ".join(parts))
