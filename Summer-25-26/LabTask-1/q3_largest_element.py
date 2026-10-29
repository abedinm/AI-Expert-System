# LabTask-1 (3): Find the largest element in a given list of integers.

n = int(input("How many numbers do you want to enter? "))

numbers = []
for i in range(n):
    numbers.append(int(input("Enter a number: ")))

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest element is:", largest)
