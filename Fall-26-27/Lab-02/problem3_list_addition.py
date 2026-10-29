# Problem 3 - Element-wise List Addition (Functions & Lists)
# Define a function that adds two lists element-wise and returns a new list.
# Example: [3, 4, 5, 1] and [6, 7, 2, 8] -> [9, 11, 7, 9]


def add_lists(list1, list2):
    result = []
    # zip() pairs up elements at the same position: (3, 6), (4, 7), ...
    for a, b in zip(list1, list2):
        result.append(a + b)
    return result


print(add_lists([3, 4, 5, 1], [6, 7, 2, 8]))
print(add_lists([1.5, 2.5], [0.5, 0.5]))
