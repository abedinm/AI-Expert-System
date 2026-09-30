# Quiz Prep — Complete Guide (from zero)
**Scope:** Selection · Genetic Algorithm (full) · 8-Queens problem
**Sources:** Lecture 4 (Local Search), Lecture 5 (Genetic Algorithm), GA example.pdf, 8Queen.pptx

---

# PART 1 — The big idea (read first, 5 min)

Everything before this chapter (BFS, DFS, UCS, A*) searched for a **path**.
Local search doesn't care about the path — **only the final state matters**.

> In the 8-queens problem, what matters is the final configuration of the queens,
> not the order in which they were added. *(Lecture 4, p7)*

**Local search:**
- keeps **one current state** (not a frontier of paths)
- moves only to **neighbours**
- doesn't remember the path

**Two advantages** *(L4 p8)*:
1. Uses very little memory — usually a **constant** amount
2. Can find reasonable solutions in **large or infinite (continuous)** state spaces

**State-space landscape** *(L4 p9–10)*: has "location" (the state) and "elevation" (the objective/cost value).
- cost function → find the **global minimum** (lowest valley)
- objective function → find the **global maximum** (highest peak)
- Convert one to the other by inserting a **minus sign**
- **Complete** = always finds a goal if one exists. **Optimal** = always finds the global max/min.

**Problem features that trap us:** local maxima · plateaux (shoulders) · ridges

---

# PART 2 — 8-QUEENS FITNESS ⭐ THE most important skill

## The encoding
- Board is 8×8. **One queen per column** (so no two queens can share a column — built into the encoding).
- Chromosome = **8 digits**. Digit *i* = **the row of the queen in column *i***.
- Example: `24748552` → column1=row2, column2=row4, column3=row7, column4=row4, column5=row8, column6=row5, column7=row5, column8=row2.

## The fitness function
**Fitness = number of NON-attacking pairs of queens.**

- Total possible pairs = **n(n−1)/2** = C(n,2)
  - 8-queens → 8×7/2 = **28**
  - 6-queens → 6×5/2 = **15**
- **Fitness = total pairs − attacking pairs**
- Solution found when **fitness = 28** (i.e. 0 attacks)

## Two queens ATTACK if:
1. **Same row** → `row[i] == row[j]`
2. **Same diagonal** → `|row[i] − row[j]| == |col[i] − col[j]|`

*(Same column is impossible — one queen per column.)*

## The counting method (from 8Queen.pptx)
Go **column by column, left to right**. For column *i*, only compare with columns to its **right** (so you never double-count).

- Column 1 has 7 comparisons, column 2 has 6, column 3 has 5 … column 8 has 0.
- 7+6+5+4+3+2+1+0 = **28** ✓

### Worked example: `24748552`
rows = [2, 4, 7, 4, 8, 5, 5, 2]

| Column | Compare with | Attacks found | Why |
|---|---|---|---|
| 1 (row 2) | cols 2–8 | **1** | col8 also row 2 → **same row** |
| 2 (row 4) | cols 3–8 | **1** | col4 also row 4 → **same row** |
| 3 (row 7) | cols 4–8 | **1** | col8 row 2: \|7−2\|=5, \|3−8\|=5 → **diagonal** |
| 4 (row 4) | cols 5–8 | 0 | — |
| 5 (row 8) | cols 6–8 | 0 | — |
| 6 (row 5) | cols 7–8 | **1** | col7 also row 5 → **same row** |
| 7 (row 5) | col 8 | 0 | — |
| 8 | — | 0 | — |

```
Attacked:      1  1  1  0  0  1  0  0   →  TOTAL = 4
Non-attacked:  6  5  4  4  3  1  1  0   →  TOTAL = 24
```

**Fitness = 28 − 4 = 24** ✅

## ⚡ THE SHORTCUT TRICK (from the AIUB Final Term video, ~28:15) — VERIFIED
Much faster than drawing the board. For each digit, scan **only to the right** and do **3 checks**:

| Check | Meaning | Rule (step = how far right you've moved) |
|---|---|---|
| **1. Duplicate** | same row | digit to the right **equals** current digit |
| **2. Increasing count** | ↗ diagonal | count **up** as you move right (+1, +2, +3…) — if the count **matches the actual digit** there → attack |
| **3. Decreasing count** | ↘ diagonal | count **down** as you move right (−1, −2, −3…) — if it matches → attack |

### Demo on `2 4 7 4 8 5 5 2`
- **Digit 1 = `2`:** duplicate → there's a `2` at the far right ✔ **HIT**. Up-count 3,4,5,6,7,8 → no match. Down-count 1,0… → no match. → **1**
- **Digit 2 = `4`:** duplicate → another `4` two places right ✔ **HIT**. → **1**
- **Digit 3 = `7`:** no duplicate. Down-count as you move right: 6, 5, 4, 3, **2** ← and the actual digit there **is** `2` ✔ **HIT** (diagonal). → **1**
- **Digits 4 (`4`), 5 (`8`):** nothing. → **0, 0**
- **Digit 6 = `5`:** duplicate → `5` immediately right ✔ **HIT**. → **1**
- **Digits 7, 8:** nothing left to compare. → **0, 0**

**Total attacks = 4 → fitness = 28 − 4 = 24** ✅ (same answer, far quicker)

> Mathematically this is identical to `|Δrow| == |Δcol|` — it's just easier to do in your head under exam pressure. **Verified to match brute force on all 9 exercise chromosomes.**

## The four AIMA states (Lecture 4, p26) — VERIFIED
| Chromosome | Attacks | Fitness | Probability |
|---|---|---|---|
| 24748552 | 4 | **24** | 24/78 = **31 %** |
| 32752411 | 5 | **23** | 23/78 = **29 %** |
| 24415124 | 8 | **20** | 20/78 = **26 %** |
| 32543213 | 17 | **11** | 11/78 = **14 %** |
| | | **Total 78** | 100 % |

---

# PART 3 — Genetic Algorithm (the full cycle)

## Definition (memorize — L4 p23)
> A genetic algorithm is a variant of **stochastic beam search** in which successor states are
> generated by **combining two parent states** rather than by modifying a single state.

## The cycle
```
   Initialize Population
            ↓
      Evaluate Fitness
            ↓
    ┌── 1. SELECTION ───────┐
    │   2. CROSSOVER        │   ← repeat until termination
    │   3. MUTATION         │
    │   4. SURVIVAL/ACCEPT  │
    └── Update Population ──┘
            ↓
   Termination condition met? → return best individual
```

## Pseudocode (AIMA / L5 p9)
```
function GENETIC-ALGORITHM(population, FITNESS-FN) returns an individual
  repeat
      new_population ← empty set
      for i = 1 to SIZE(population) do
          x ← RANDOM-SELECTION(population, FITNESS-FN)
          y ← RANDOM-SELECTION(population, FITNESS-FN)
          child ← REPRODUCE(x, y)
          if (small random probability) then child ← MUTATE(child)
          add child to new_population
      population ← new_population
  until some individual is fit enough, or enough time has elapsed
  return the best individual in population

function REPRODUCE(x, y) returns an individual
  n ← LENGTH(x)
  c ← random number from 1 to n
  return APPEND(SUBSTRING(x, 1, c), SUBSTRING(y, c+1, n))
```

## ENCODING — 3 types (L5 p10–15)
| Type | Chromosome looks like | Used for |
|---|---|---|
| **Binary** | `10110` | numeric optimization, knapsack |
| **Value** | `1.23  5.67  0.89` or `ABDJE` | when binary is unnatural (real numbers, weights) |
| **Permutation** | `1 5 3 2 6 4 7 9 8` | ordering problems — TSP, task scheduling |

---

# PART 4 — SELECTION ⭐ (named topic)

**Purpose:** choose parents for reproduction — fitter individuals should get more chances,
but weak ones must keep *some* chance (else we lose diversity and converge prematurely).

## Roulette Wheel (fitness-proportionate) — the one they'll test
Each individual gets a slice of the wheel proportional to its fitness.

**Formula: P(i) = fᵢ / Σf**

**Procedure:**
1. Compute fitness of every individual
2. Compute total fitness Σf
3. P(i) = fᵢ / Σf
4. Build **cumulative** ranges (bins)
5. Generate a random number in [0,1] → whichever bin it falls in, that individual is selected

## "Best Selection" — the simple alternative (AIUB video, ~13:25) ⭐
> Choose the **top N parents by fitness alone** — **no bins, no random numbers.**

If asked to "select 4 parents by best selection" from fitness 108, 123.5, 195.5, 56, 0, 27.5 →
just take the four highest: **195.5, 123.5, 108, 56** (chromosomes 3, 2, 1, 4).
Notice this happens to give the *same* four parents as the roulette wheel did in the worked example — but by a completely different route. **Read the question to see which method is being asked for.**

## Other methods
| Method | How | Advantage |
|---|---|---|
| **Tournament** | pick *k* at random, fittest of them wins | simple; pressure tunable via *k* |
| **Rank** | sort by fitness, select by **rank** not raw value | stops a "super-individual" dominating |
| **Elitism** | copy the best *n* directly to next generation | best solution is never lost |
| **Truncation** | keep top x %, breed only from those | crude but fast |
| **SUS** | one spin, evenly-spaced pointers | lower variance than roulette |

**Selection pressure:** too high → premature convergence (stuck in a local optimum);
too low → search becomes nearly random and slow.

---

# PART 5 — CROSSOVER (6 types, L5 p26–31)

Let P1 = `1 1 0 1 0 1`, P2 = `0 0 1 0 1 0`

| Type | How it works | Example |
|---|---|---|
| **One-point** | pick 1 point, swap tails | P1=`110\|101`, P2=`001\|010` → `110010`, `001101` |
| **Two-point** | pick 2 points, swap the middle | `11\|01\|01` + `00\|10\|10` → `111001`, `000110` |
| **Uniform** | each gene chosen from P1 or P2 by coin flip / mask | mask `101010` → take genes 1,3,5 from P1, rest from P2 |
| **Arithmetic** | apply an arithmetic op (e.g. AND, or weighted average) | `α·P1 + (1−α)·P2` for real values |
| **Heuristic** | uses **fitness** to guide the child, extrapolating from the better parent | child = best + r·(best − worst) |
| **Three-parent** | needs P1, P2, P3 (see rule below) | — |

### Three-Parent Crossover rule (L5 p31) — distinctive, likely asked
For each bit position:
- **if P1 == P2 → take P1**
- **if P1 ≠ P2 → take P3**

```
P1: 0 1 1 0 1 0
P2: 1 1 0 1 0 0
P3: 1 0 0 1 0 1
--------------------
O1: 1 1 0 1 1 0
```
Check bit 1: P1=0, P2=1 → differ → take P3=1 ✓
Bit 2: P1=1, P2=1 → same → take P1=1 ✓
Bit 5: P1=1, P2=0 → differ → take P3=0 … *(slide shows 1; follow the slide's own answer in the exam)*

*For O2 and O3, repeat with the orders (P1,P3,P2) and (P2,P3,P1).*

---

# PART 6 — MUTATION

**Purpose:** maintain diversity, escape local optima. Applied with **low probability** (e.g. 1 %).

- **Flip-bit mutation** (binary): pick a random position, flip 0↔1
  `1 0 1 1 0` → flip position 2 → `1 1 1 1 0`
- **Value encoding:** add/subtract a small random value
- **Permutation encoding:** swap two positions (can't just flip — must stay a valid permutation)

---

# PART 7 — THE NUMERICAL EXAMPLE (GA example.pdf + L4 p38–42) ⭐⭐
### Maximize f(x) = x²/2 − 3x, x ∈ [0, 31], binary encoding, 5 digits

Why 5 bits? Because 2⁵ = 32 values → covers 0…31 exactly.

## Step 0 — Initial population & fitness (VERIFIED)
| # | Chromosome | x | f(x) = x²/2 − 3x | Probability | Cumulative bin |
|---|---|---|---|---|---|
| 1 | 10010 | 18 | 162 − 54 = **108** | 0.211 | 0.001 – 0.211 |
| 2 | 10011 | 19 | 180.5 − 57 = **123.5** | 0.242 | 0.212 – 0.453 |
| 3 | 10111 | 23 | 264.5 − 69 = **195.5** | 0.383 | 0.454 – 0.836 |
| 4 | 01110 | 14 | 98 − 42 = **56** | 0.110 | 0.837 – 0.946 |
| 5 | 00101 | 5 | 12.5 − 15 = −2.5 → **0** ⚠️ | 0 | — |
| 6 | 01011 | 11 | 60.5 − 33 = **27.5** | 0.054 | 0.947 – 1.00 |
| | | | **Total = 510.5** | 1.00 | |

⚠️ **The trap:** string 5 gives a **negative** value → clamped to **0**, and it gets **no roulette slice**.

## Step 1 — Selection (4 parents, randoms 0.54, 0.88, 0.45, 0.20) — VERIFIED
| Random | Falls in bin | Selected parent |
|---|---|---|
| 0.54 | 0.454–0.836 | #3 `10111` |
| 0.88 | 0.837–0.946 | #4 `01110` |
| 0.45 | 0.212–0.453 | #2 `10011` |
| 0.20 | 0.001–0.211 | #1 `10010` |

## Step 2 & 3 — Crossover, then Mutation (1 % chance)
| Parent | After crossover | After mutation |
|---|---|---|
| `10111` | `10110` | **`11110`** |
| `01110` | `01111` | `01111` |
| `10011` | `10010` | `10010` |
| `10010` | `10011` | `10011` |

## Step 4 — Accept / Survival (VERIFIED)
| Offspring | x | Fitness |
|---|---|---|
| **11110** | 30 | **360** ⭐ big improvement |
| 01111 | 15 | 67.5 |
| 10010 | 18 | 108 |
| 10011 | 19 | 123.5 |

## Step 5 — Updated population → 7 strings → **check termination** → new cycle

---

# PART 8 — Local search algorithms (context, L4 p11–22)

## Hill Climbing (steepest-ascent) — L4 p12
> "A loop that continually moves in the direction of **increasing value** — that is, uphill.
> It terminates when it reaches a peak where no neighbour has a higher value."

Gets stuck on: **Local maxima · Ridges · Plateaux**

### Variants (L4 p13–14)
| Variant | Behaviour |
|---|---|
| **Steepest-ascent** | picks the **best** neighbour |
| **Stochastic** | picks **randomly** among uphill moves (prob. can vary with steepness); slower but sometimes better solutions |
| **First-choice** | generates successors randomly until one is **better** than current — good when there are **thousands** of successors |
| **Random-restart** | *"If at first you don't succeed, try, try again."* Repeats hill climbing from random starts until a goal is found |

**8-queens performance:** plain hill climbing solves **~14 %**; with sideways moves **~94 %**;
random-restart expected restarts = **1/p ≈ 7**, ≈ 22 steps total.

## Simulated Annealing — L4 p17
Combines hill climbing with a random walk → **both efficiency and completeness**.
Allows **downhill** moves with probability that decreases as temperature **T** falls.

**P(accept bad move) = e^(ΔE/T)**, where ΔE = E(successor) − E(current)
Accept the bad move only if **random < P**. (Uphill moves are always accepted.)

## Local Beam Search — L4 p21
- Keeps **k states**, not 1.
- Start with k random states → generate **all** successors of all k → if any is a goal, stop → else keep the **k best** overall, repeat.
- **Stochastic beam search:** choose k successors **at random** (probability ∝ fitness) → this is GA's direct ancestor.

## Continuous spaces — L4 p31–35 (lowest priority)
- Gradient: ∇f = (∂f/∂x₁, ∂f/∂y₁, …); solve ∇f = 0
- **Gradient ascent/descent:** `x ← x + α∇f(x)`; α = step size (too small → too many steps; too large → overshoot)
- **Newton–Raphson:** `x ← x − H⁻¹f(x)·∇f(x)`, H = Hessian matrix of second derivatives

---

# PART 9 — PRACTICE PROBLEMS (with verified answers)

## Q1 — 8-queens attack count (Lecture 4, p28)
**Find the number of attacks on `76012345` and `66743210`.**

<details>
**`76012345`** → rows [7,6,0,1,2,3,4,5]
- Columns 3–8 hold rows 0,1,2,3,4,5 → a perfect diagonal → every pair attacks → C(6,2) = **15**
- Plus column1 (row7) vs column2 (row6): |7−6| = 1 = |1−2| → diagonal → **1**
- **Total attacks = 16**, fitness = 28 − 16 = **12**

**`66743210`** → rows [6,6,7,4,3,2,1,0]
- **Total attacks = 17**, fitness = 28 − 17 = **11**
(per-column attacks: 1, 6, 0, 4, 3, 2, 1, 0)
</details>

## Q2 — 6-queens fitness (Lecture 4, p37)
**Calculate fitness (non-attacking pairs) for `211345`, `403234`, `511023`. Columns start at 0. Max = 15.**

<details>

| Chromosome | rows | Attacks | **Fitness** |
|---|---|---|---|
| `211345` | [2,1,1,3,4,5] | 8 | **7** |
| `403234` | [4,0,3,2,3,4] | 9 | **6** |
| `511023` | [5,1,1,0,2,3] | 3 | **12** ← fittest |

per-column attacks:
- 211345 → [1, 4, 0, 2, 1, 0]
- 403234 → [1, 3, 2, 2, 1, 0]
- 511023 → [0, 1, 1, 0, 1, 0]
</details>

## Q3 — Simulated annealing (Lecture 4, p20)
**Maximization. S = 100, T = 10. Successors A(95, 0.65), B(105, 0.8), C(90, 0.5), D(85, 0.2).
Which are accepted?**

<details>

| Node | E | ΔE | P = e^(ΔE/T) | Random | Verdict |
|---|---|---|---|---|---|
| A | 95 | −5 | e^(−0.5) = **0.6065** | 0.65 | 0.65 > 0.6065 → **REJECT** |
| B | 105 | **+5** | uphill — always accept | 0.8 | **ACCEPT** |
| C | 90 | −10 | e^(−1) = **0.3679** | 0.5 | 0.5 > 0.3679 → **REJECT** |
| D | 85 | −15 | e^(−1.5) = **0.2231** | 0.2 | 0.2 < 0.2231 → **ACCEPT** |

**Accepted: B and D.**
*Note: the slide writes the probability as "ΔE/T" — that's shorthand for e^(ΔE/T).*
</details>

## Q4 — Roulette wheel
**Fitness values 24, 23, 20, 11. Find each selection probability. Random = 0.60 → who is selected?**

<details>
Total = 78 → 24/78 = **0.31**, 23/78 = **0.29**, 20/78 = **0.26**, 11/78 = **0.14**
Bins: A 0–0.31 · B 0.31–0.60 · C 0.60–0.86 · D 0.86–1.00
Random 0.60 → falls at the C boundary → **C** (the fitness-20 individual)
</details>

## Q5 — Binary GA
**Chromosome `11010`, f(x) = x²/2 − 3x. Find x and fitness.**

<details>
`11010` = 16+8+0+2+0 = **26** → f(26) = 338 − 78 = **260**
</details>

---

# PART 10 — FINAL CHECKLIST (revise 30 min before)

- [ ] Local search = path irrelevant, only final state matters; constant memory
- [ ] Landscape: local maximum, plateau/shoulder, ridge
- [ ] Hill climbing variants: steepest-ascent, stochastic, first-choice, random-restart
- [ ] SA: accept bad move with **P = e^(ΔE/T)**; accept if random < P; uphill always accepted
- [ ] Beam search keeps **k** states; stochastic beam → ancestor of GA
- [ ] **GA = stochastic beam search + two parents**
- [ ] 3 encodings: **binary, value, permutation**
- [ ] GA cycle: Initialize → Fitness → **Selection → Crossover → Mutation → Survival** → repeat
- [ ] **Roulette wheel: P(i) = fᵢ / Σf**, then cumulative bins
- [ ] 6 crossovers: one-point, two-point, uniform, arithmetic, heuristic, three-parent
- [ ] Three-parent rule: P1==P2 → P1, else → P3
- [ ] Mutation = low probability, flip-bit for binary
- [ ] **Max non-attacking pairs = n(n−1)/2** → 8-queens **28**, 6-queens **15**
- [ ] Attack test: **same row** or **|Δrow| == |Δcol|**
- [ ] `24748552` → 4 attacks → fitness **24**; the four states are **24, 23, 20, 11** (total 78 → 31 %)
- [ ] f(x) = x²/2 − 3x: 5-bit encoding, **negative fitness clamped to 0**, best offspring `11110` → x=30 → **360**
- [ ] ⚠️ Hill climbing **minimizes attacks** (h→0); GA **maximizes non-attacking pairs** (fitness→28)
