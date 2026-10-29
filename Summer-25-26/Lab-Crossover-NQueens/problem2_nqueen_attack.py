# Problem 2 - N Queen attack detection

n = int(input("Enter the dimension of the board (N): "))
total = int(input("How many queens are placed? "))

queens = []
for q in range(total):
    pos = input("Position of queen " + str(q + 1) + " (row,col): ").split(",")
    queens.append((int(pos[0]), int(pos[1])))

print()
print("Board size:", n, "x", n)
print("Queens:", queens)
print()

attacks = 0

# check every pair of queens once
for a in range(len(queens)):
    for b in range(a + 1, len(queens)):
        i, j = queens[a]
        k, l = queens[b]

        if i == k:
            result = "Row attack"
        elif j == l:
            result = "Column attack"
        elif abs(j - l) == abs(k - i):     # diagonal rule from the slide
            result = "Diagonal attack"
        else:
            result = "No attack"

        if result != "No attack":
            attacks = attacks + 1

        print(queens[a], "and", queens[b], "->", result)

print()
print("Total number of attacks:", attacks)
