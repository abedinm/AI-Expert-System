

def process_numbers(numbers):
    unique = set(numbers)                            # 1. remove duplicates (a set has no repeats)
    sorted_desc = sorted(unique, reverse=True)       # 2. sort descending
    result = [n for n in sorted_desc if n % 3 != 0]  # 3. filter OUT multiples of 3
    return result                                    # 4. return modified list


def main():
    raw = input("Enter integers (space or comma separated): ")
    numbers = [int(x) for x in raw.replace(",", " ").split()]
    print("Original list :", numbers)
    print("Modified list :", process_numbers(numbers))


if __name__ == "__main__":
    main()
