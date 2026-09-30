# Lab-01 Study Material
**Course:** CSC4226 — Artificial Intelligence and Expert System
**Topics:** Set, Tuple, Dictionary + List processing + Matrix multiplication

---

## PART A — Core Data Structures (study these first)

Python has four built-in collection types. Knowing how they differ is the whole point of the warm-up.

| Feature        | **List** `[]` | **Tuple** `()` | **Set** `{}` | **Dictionary** `{k:v}` |
|----------------|---------------|----------------|--------------|------------------------|
| Ordered        | Yes (indexed) | Yes (indexed)  | **No**       | Yes (insertion order, 3.7+) |
| Mutable        | Yes           | **No**         | Yes          | Yes |
| Duplicates     | Allowed       | Allowed        | **Not allowed** | Keys unique; values can repeat |
| Access by      | index `l[0]`  | index `t[0]`   | membership `x in s` | key `d["x"]` |
| Written with   | `[1, 2, 3]`   | `(1, 2, 3)`    | `{1, 2, 3}`  | `{"a": 1}` |

---

### 1. Set

A **set** is an unordered collection of **unique** items. Because it cannot hold duplicates, it is the natural tool for de-duplication (used in Task 1).

```python
s = {1, 2, 2, 3}        # -> {1, 2, 3}   duplicate dropped automatically
empty = set()           # NOT {}  ({} makes an empty DICTIONARY)

# Add / remove
s.add(4)                # {1, 2, 3, 4}
s.discard(10)           # safe: no error if 10 is missing
s.remove(2)             # error if 2 is missing
s.pop()                 # removes an arbitrary element
s.clear()               # empties the set

# Membership test is very fast (O(1) average)
3 in {1, 2, 3}          # True
```

**Set algebra** (think Venn diagrams):

```python
A = {1, 2, 3}
B = {3, 4, 5}
A | B    # union          -> {1, 2, 3, 4, 5}
A & B    # intersection   -> {3}
A - B    # difference     -> {1, 2}
A ^ B    # symmetric diff -> {1, 2, 4, 5}
```

- A `frozenset(...)` is an **immutable** set (can be used as a dict key / set element).
- Sets are unordered, so you **cannot** index them: `s[0]` is an error.

---

### 2. Tuple

A **tuple** is an ordered, **immutable** sequence. Use it for fixed groups of values that should not change (coordinates, RGB colors, a database record).

```python
t = (10, 20, 30)
t[0]                    # 10   (indexing works like a list)
t[-1]                   # 30   (negative index = from the end)
t[0:2]                  # (10, 20)  slicing
# t[0] = 99             # ERROR: tuples are immutable

# Packing & unpacking (very common)
point = 4, 5            # packing -> (4, 5)
x, y = point            # unpacking -> x=4, y=5
a, b = b, a             # swap without a temp variable

# A single-element tuple NEEDS a trailing comma
one = (5,)              # tuple
not_tuple = (5)         # this is just the int 5

# Only two methods (because it's immutable)
(1, 2, 2, 3).count(2)   # 2
(1, 2, 3).index(3)      # 2  (position of value 3)
```

**Tuple vs List:** use a tuple when the data is fixed and you want it protected from accidental change; use a list when you need to add/remove/sort items.

---

### 3. Dictionary

A **dictionary** maps **keys → values**. Keys must be unique and immutable (str, int, tuple); values can be anything.

```python
d = {"name": "Joy", "age": 22}

# Access
d["name"]               # "Joy"
d.get("city")           # None  (no KeyError, unlike d["city"])
d.get("city", "N/A")    # "N/A" (default if missing)

# Add / update
d["city"] = "Dhaka"     # add new key
d["age"] = 23           # update existing key
d.update({"age": 24, "dept": "CS"})   # bulk update

# Delete
del d["dept"]           # remove a key
d.pop("city")           # remove and return its value
d.popitem()             # remove & return the last inserted pair

# Views & iteration
d.keys()                # dict_keys(['name', 'age'])
d.values()              # dict_values(['Joy', 24])
d.items()               # dict_items([('name','Joy'), ('age',24)])

for key, value in d.items():
    print(key, "=", value)

# Dict comprehension
squares = {n: n*n for n in range(1, 4)}   # {1: 1, 2: 4, 3: 9}
```

Dictionaries are ideal for lookups by name/id, counting frequencies, and grouping data.

---

## PART B — Concepts for Task 1 (clean → dedupe → sort → filter)

> Task: take integers from the user, remove duplicates, sort descending, filter OUT multiples of 3, return the list.

### B.1 Lists
```python
nums = [9, 3, 3, 7]
nums.append(5)          # add to end
nums[0]                 # 9 (indexed access)
len(nums)               # length
```

### B.2 Removing duplicates with a set
Convert the list to a `set` (drops repeats), then back if needed:
```python
unique = set([9, 3, 3, 7])     # {9, 3, 7}
```

### B.3 Sorting — `sorted()` vs `.sort()`
| | Returns new? | Modifies original? |
|---|---|---|
| `sorted(x, reverse=True)` | Yes (new list) | No |
| `x.sort(reverse=True)`    | No (returns None) | Yes (in place) |

```python
sorted({9, 3, 7}, reverse=True)   # [9, 7, 3]   descending
```
> `sorted()` accepts ANY iterable (incl. a set) and always returns a **list** — that's why it fits perfectly after `set(...)`.

### B.4 The modulo operator `%` (the divisibility test)
`a % b` is the remainder of `a ÷ b`.
```python
12 % 3    # 0  -> divisible by 3
7  % 3    # 1  -> NOT divisible by 3
```
So **"divisible by 3"** is `n % 3 == 0`, and **"keep the ones NOT divisible by 3"** (what "filter out multiples of 3" means) is `n % 3 != 0`.

### B.5 List comprehension (filtering)
A compact `[expression for item in iterable if condition]`:
```python
[n for n in [9, 7, 6, 5] if n % 3 != 0]   # [7, 5]   keeps non-multiples of 3
```

### Putting it together
```python
unique      = set(numbers)                       # dedupe
sorted_desc = sorted(unique, reverse=True)       # sort high -> low
result      = [n for n in sorted_desc if n % 3 != 0]   # drop multiples of 3
```

---

## PART C — Concepts for Task 2 (matrix multiplication)

### C.1 A matrix is a list of lists (2D list)
```python
A = [[1, 2, 3],
     [4, 5, 6]]      # 2 rows, 3 columns  -> a 2x3 matrix
A[0]        # [1, 2, 3]   first row
A[1][2]     # 6           row 1, column 2  ->  A[row][col]
len(A)      # 2  (number of rows)
len(A[0])   # 3  (number of columns)
```

### C.2 The multiplication rule
To compute **A × B**:
- **Columns of A must equal rows of B.** `(m×n) × (n×p)` is valid.
- The **result is m×p** (rows of A by columns of B).

```
A: 2x3      B: 3x2      ->  A×B: 2x2
```

### C.3 How each cell is computed (dot product)
Cell `(i, j)` of the result = the dot product of **row i of A** with **column j of B**:

```
result[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][n-1]*B[n-1][j]
```

Example: `result[0][0] = 1*7 + 2*9 + 3*11 = 58`.

### C.4 The triple-nested-loop algorithm
```python
result = [[0] * cols_B for _ in range(rows_A)]   # start with a zero matrix
for i in range(rows_A):          # pick the result row  (row of A)
    for j in range(cols_B):      # pick the result column (column of B)
        for k in range(cols_A):  # walk the shared dimension, summing products
            result[i][j] += A[i][k] * B[k][j]
```
- Outer two loops choose **which output cell** `(i, j)`.
- Inner `k` loop builds that cell's **dot product**.
- Build the zero matrix with `[[0]*cols for _ in range(rows)]` — **not** `[[0]*cols]*rows`, which makes shared (aliased) rows that all change together.

### C.5 Complexity
Three nested loops over m, p, n → **O(m·n·p)** time (O(n³) for square n×n matrices).
*(For real numerical work you'd use NumPy: `import numpy as np; np.array(A) @ np.array(B)` — but writing the loops shows you understand the algorithm, which is the point of this lab.)*

---

## Quick revision checklist
- [ ] Set = unordered, unique, mutable; `{}` is a dict, use `set()` for an empty set.
- [ ] Tuple = ordered, **immutable**; single element needs a comma `(5,)`.
- [ ] Dict = key→value; `.get()` avoids KeyError; iterate with `.items()`.
- [ ] `n % 3 == 0` means divisible by 3.
- [ ] `sorted(x, reverse=True)` returns a new descending list from any iterable.
- [ ] Matrix mult: cols(A) == rows(B); result is rows(A) × cols(B); cell = dot product.

**Reference:** W3Schools — Python Sets / Tuples / Dictionaries; TutorialsPoint — Python Data Structures.
