# Problem 4 - Unique Word Counter (Sets & Strings)
# Split a paragraph into words and use a set to count the unique words (case-insensitive).

PUNCTUATION = ".,!?;:\"'()"


def count_unique_words(text):
    words = text.lower().split()
    cleaned = []
    for word in words:
        # strip punctuation so "search." and "search" count as the same word
        cleaned.append(word.strip(PUNCTUATION))
    unique = set(cleaned)
    unique.discard("")         # in case a "word" was only punctuation
    return len(unique)


paragraph = "AI is fun. Search is part of AI, and search is fun to learn!"
print("Paragraph:", paragraph)
print("Unique words:", count_unique_words(paragraph))
# unique: ai, is, fun, search, part, of, and, to, learn -> 9
