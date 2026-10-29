# Problem 6 - Character Frequency Counter (Dictionaries & Strings)
# Return a dictionary counting how often each character appears in a string.


def char_frequency(text):
    freq = {}
    for char in text:
        # get() returns 0 the first time a character is seen
        freq[char] = freq.get(char, 0) + 1
    return freq


print(char_frequency("hello world"))
print(char_frequency("mississippi"))
