# Final Term — Practice Problems
Alpha-Beta Pruning · CSP · Bayesian Networks

**Attempt everything before scrolling to the solutions.** Every answer below was computed and
checked in code, so if you disagree with one, you have found a real mistake in your working.

---

# PART A — ALPHA-BETA PRUNING

### A1
MAX root, three MIN children. Leaves left to right:
```
[5, 6, 7]   [4, 5, 3]   [6, 6, 9]
```
(a) What value does the root return?
(b) Which leaves are pruned?
(c) How many leaves are examined?

### A2
MAX root, **four** MIN children, two leaves each:
```
[3, 5]   [6, 9]   [1, 2]   [0, 7]
```
(a) Root value? (b) Pruned leaves?

### A3
Same nine leaves as A1, but the branches are reordered:
```
[6, 6, 9]   [4, 5, 3]   [5, 6, 7]
```
(a) Does the root value change?
(b) How many leaves are pruned now?
(c) What does the comparison with A1 tell you?

### A4
Now the **root is MIN** and its children are MAX nodes:
```
[2, 3]   [5, 9]   [0, 1]
```
(a) Root value? (b) Pruned leaves? (c) Which variable does the root update, α or β?

### A5 — short answer
(a) Can alpha-beta ever return a different value from plain minimax?
(b) What is the pruning condition?
(c) With perfect move ordering, what is the time complexity?

---

# PART B — CONSTRAINT SATISFACTION

A map has five regions **A, B, C, D, E**. These pairs are adjacent:
```
A-B   A-C   B-C   B-D   C-D   C-E   D-E
```
Domain of every region: **{R, G, B}**. Adjacent regions must differ.

### B1
Draw the constraint graph and give the **degree** of each variable.

### B2
Assign **A = R**. Apply forward checking — what are the remaining domains?
Which variable does **MRV** select? If there is a tie, break it with the **degree heuristic**.

### B3
Continue: **A = R, B = G**. Forward-check again.
Remaining domains? MRV choice?

### B4
Continue: **A = R, B = G, D = R**. Forward-check.
Remaining domains? Is the assignment still viable?

### B5 — short answer
(a) What is the difference between MRV and the degree heuristic?
(b) When does forward checking tell you to backtrack?
(c) Why is a region with no neighbours (an island) trivial in a CSP?

---

# PART C — BAYESIAN NETWORKS

Network:
```
            Cloudy
           /      \
    Sprinkler     Rain
           \      /
           WetGrass
```
```
P(C) = 0.5
P(S|C)  = 0.10      P(S|¬C) = 0.50
P(R|C)  = 0.80      P(R|¬C) = 0.20
P(W|S,R)  = 0.99    P(W|S,¬R)  = 0.90
P(W|¬S,R) = 0.90    P(W|¬S,¬R) = 0.00
```

### C1
Compute **P(c, s, ¬r, w)** — cloudy, sprinkler on, no rain, grass wet.

### C2
Compute **P(¬c, s, r, w)**.

### C3
Compute **P(w)** — the probability the grass is wet, with nothing else given.

### C4
Compute **P(c | w)** — given the grass is wet, how likely is it cloudy?

### C5
Compute **P(r)** — the probability of rain, nothing given.

### C6 — short answer
(a) Which nodes are the parents of WetGrass?
(b) Why is P(W|¬S,¬R) = 0 sensible?
(c) When must you sum over a variable?

---
---

# SOLUTIONS

## PART A — Alpha-Beta

### A1  →  value **6**, pruned **5 and 3**, examined **7 of 9**
- MIN₁ sees 5, 6, 7 → returns **5**. Root α = 5.
- MIN₂ sees 4. Since 4 ≤ α(5), MIN₂ can only get worse for MAX → **prune 5 and 3**.
- MIN₃ sees 6, 6, 9 → returns **6**. Root α = 6.
- Root = max(5, 4, 6) = **6**

Examined: 5, 6, 7, 4, 6, 6, 9

### A2  →  value **6**, pruned **2 and 7**, examined **6 of 8**
- MIN₁ → 3. α = 3
- MIN₂ sees 6 (> α, continue), then 9 → returns **6**. α = 6
- MIN₃ sees 1 ≤ α(6) → **prune 2**
- MIN₄ sees 0 ≤ α(6) → **prune 7**
- Root = max(3, 6, 1, 0) = **6**

### A3  →  value still **6**, but **4 leaves pruned**, only **5 of 9** examined
- MIN₁ sees 6, 6, 9 → **6**. α = 6 straight away.
- MIN₂ sees 4 ≤ 6 → **prune 5, 3**
- MIN₃ sees 5 ≤ 6 → **prune 6, 7**

**(c) This is the lesson of the whole topic.** Identical leaves, identical answer — but putting
the strong branch first raised α early and doubled the pruning (2 → 4 leaves).
**Move ordering decides how much alpha-beta saves.** It never changes the result.

### A4  →  value **1**, pruned **9**, examined **5 of 6**
Root is MIN, so it updates **β**.
- MAX₁ sees 2, 3 → **3**. Root β = 3
- MAX₂ sees 5. Since 5 ≥ β(3) → **prune 9**
- MAX₃ sees 0, 1 → **1**
- Root = min(3, 5, 1) = **1**

### A5
**(a) No — never.** Alpha-beta returns exactly the minimax value. It only avoids work.
**(b) Prune when α ≥ β.**
**(c) O(b^(m/2))** with perfect ordering, versus O(bᵐ) for plain minimax — so you can search
roughly **twice as deep** in the same time.

---

## PART B — CSP

### B1 — degrees
| Variable | Neighbours | Degree |
|---|---|---|
| **C** | A, B, D, E | **4** ← most constrained |
| B | A, C, D | 3 |
| D | B, C, E | 3 |
| A | B, C | 2 |
| E | C, D | 2 |

### B2 — after **A = R**
```
B {G, B}      C {G, B}      D {R, G, B}      E {R, G, B}
```
B and C both drop to 2 values → **MRV ties between B and C**.
Break with the degree heuristic: **C has 4 neighbours, B has 3 → choose C.**

*(This is exactly the situation the degree heuristic exists for.)*

### B3 — after **A = R, B = G**
```
C {B}      D {R, B}      E {R, G, B}
```
C is down to a single value → **MRV picks C**, no tie this time.
C loses R (from A) and G (from B), leaving only Blue.

### B4 — after **A = R, B = G, D = R**
```
C {B}      E {G, B}
```
**Still viable** — no domain is empty. C must be B; E may be G or B, and once C = B, E must be G.
A full solution: **A=R, B=G, C=B, D=R, E=G.**

### B5
**(a)** **MRV counts the values a variable has left** — pick the smallest domain, so failures
surface early. **Degree counts neighbours among unassigned variables** — it is the tie-breaker,
used mainly at the start when every domain is still full size.

**(b)** The moment **any domain becomes empty**. That assignment cannot lead to a solution, so
undo it immediately rather than searching further.

**(c)** An island has **no constraints on it**, so any colour works. It can be assigned last,
arbitrarily, and never causes backtracking. (Tasmania, in the Australia example.)

---

## PART C — Bayesian Networks

Every joint is the product of each node given its parents — **follow the arrows downward.**

### C1  →  **0.00900**
```
P(c, s, ¬r, w) = P(c) × P(s|c) × P(¬r|c) × P(w|s,¬r)
               = 0.5  × 0.10   × 0.20    × 0.90
               = 0.009
```
Note `P(¬r|c) = 1 − 0.80 = 0.20`.

### C2  →  **0.04950**
```
P(¬c, s, r, w) = P(¬c) × P(s|¬c) × P(r|¬c) × P(w|s,r)
               = 0.5   × 0.50    × 0.20    × 0.99
               = 0.0495
```

### C3  →  **P(w) = 0.64710**
W is not a root, and C, S, R are all unfixed — so **sum over all eight combinations** of
(C, S, R) with W true:
```
P(w) = Σ over c,s,r of  P(c)·P(s|c)·P(r|c)·P(w|s,r)   =  0.6471
```

### C4  →  **P(c | w) = 0.57580**
Conditional ⇒ **normalise**:
```
P(c | w) = P(c, w) / P(w)

P(c, w) = Σ over s,r of P(c)·P(s|c)·P(r|c)·P(w|s,r) = 0.3726
P(w)                                                = 0.6471

P(c | w) = 0.3726 / 0.6471 = 0.5758
```
Sensible: wet grass raises the chance of cloudy from 0.5 to about 0.58.

### C5  →  **P(r) = 0.50000**
Only C matters, so sum over it:
```
P(r) = P(r|c)·P(c) + P(r|¬c)·P(¬c)
     = 0.80 × 0.5  + 0.20 × 0.5
     = 0.40 + 0.10 = 0.50
```

### C6
**(a)** Sprinkler and Rain. (Cloudy is a *grand*parent — it affects W only through them.)
**(b)** If the sprinkler is off and it has not rained, nothing has wet the grass, so the
probability is 0.
**(c)** Whenever a variable appears in the network but is **not fixed by the question** —
it is a hidden variable, so sum over all of its values.

---

# Marking yourself

| | Score | What it means |
|---|---|---|
| Part A | /5 | Under 3 → redo A1 and A3 until the pruning is automatic |
| Part B | /5 | Missing B2 usually means MRV/degree are still blurred |
| Part C | /6 | C3 and C4 are the hard ones — marginalise, then normalise |

**The three mistakes that cost the most marks:**
1. Forgetting `P(¬X) = 1 − P(X)` on a negative term
2. Confusing MRV (fewest values) with degree (most neighbours)
3. Pruning on α > β instead of **α ≥ β**
