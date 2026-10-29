# Lab-01 Cheatsheet — Set · Tuple · Dict + the 2 tasks

## At a glance
| | List `[]` | Tuple `()` | Set `{}` | Dict `{k:v}` |
|---|---|---|---|---|
| Ordered | yes | yes | **no** | yes |
| Mutable | yes | **no** | yes | yes |
| Duplicates | yes | yes | **no** | unique keys |
| Access | `l[0]` | `t[0]` | `x in s` | `d["k"]` |

## Set — unique, unordered
```python
s = {1,2,2,3}      # {1,2,3}      set()  # empty ({} is a dict!)
s.add(4); s.discard(9)            # discard=safe, remove=errors
A|B  A&B  A-B  A^B                # union, intersect, diff, sym-diff
```

## Tuple — immutable
```python
t=(10,20,30); t[0]; t[-1]; t[1:]  # index/slice
x,y = (4,5)        # unpack        one=(5,)  # 1-elem needs comma
t.count(2); t.index(3)            # only 2 methods
```

## Dict — key→value
```python
d={"name":"Joy"}; d["name"]
d.get("city","N/A")               # no KeyError
d["age"]=22; d.update({...}); d.pop("age"); del d["name"]
for k,v in d.items(): ...
```

## Task 1 — dedupe → sort↓ → drop ÷3
```python
n % 3 == 0          # divisible by 3   (!= 0 keeps non-multiples)
unique = set(numbers)
desc   = sorted(unique, reverse=True)        # new list, any iterable
result = [n for n in desc if n % 3 != 0]
```

## Task 2 — matrix multiply (A m×n · B n×p → m×p)
```python
# rule: cols(A) == rows(B);  cell = dot product of row i, col j
result = [[0]*cols_B for _ in range(rows_A)]   # NOT [[0]*c]*r (aliases!)
for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):
            result[i][j] += A[i][k]*B[k][j]
# 1*7 + 2*9 + 3*11 = 58 ;  O(m·n·p)
```
