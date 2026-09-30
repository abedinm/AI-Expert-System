# Quiz Prep — Selection · Genetic Algorithm (full) · 8-Queens
Course: Artificial Intelligence and Expert System · Source: AIMA (Russell & Norvig) Ch. 4 — Beyond Classical Search

---

## 1. Where this sits: Local Search

Classical search (BFS/DFS/UCS) cares about the **path**. Local search cares only about the **final state** — the path is irrelevant (8-queens, TSP, scheduling).

- Keeps **one current state** (or a few), moves to neighbours, doesn't keep the whole frontier.
- **Advantages:** very little memory; works in huge/infinite state spaces.
- **Objective function:** maximize (fitness) or minimize (cost/heuristic).

**Landscape vocabulary:** global maximum, local maximum, plateau / shoulder, ridge.

### Hill Climbing ("greedy local search")
Always move to the best neighbour; stop when no neighbour is better.
- **Gets stuck on:** local maxima, plateaux, ridges.
- **Variants:** steepest-ascent · stochastic · first-choice · **random-restart** (keep restarting from random states — "if at first you don't succeed, try, try again").

### Simulated Annealing
Allows *bad* moves with probability `e^(ΔE/T)`; temperature **T** decreases over time. High T → nearly random walk; low T → nearly hill climbing. Complete & optimal if T lowered slowly enough.

### Local Beam Search
Keeps **k states** (not 1). Generates all successors, keeps the best k overall. *Stochastic beam search* picks successors with probability ∝ fitness — this is the direct ancestor of GA.

---

## 2. The 8-Queens Problem ⭐

Place 8 queens on an 8×8 board so **no two attack each other** (same row, column, or diagonal).

### Formulation (complete-state, for local search)
| Item | Definition |
|---|---|
| **State** | 8 queens, **one per column** (column constraint built in) |
| **State space** | 8⁸ ≈ **17 million** states (one queen per column) |
| **Successors** | move one queen to another square **in its own column** → 8 × 7 = **56 successors** |
| **Cost / heuristic h** | number of **pairs of queens attacking each other** (directly or indirectly) |
| **Goal** | **h = 0** |

> If queens could go anywhere: C(64,8) ≈ 4.4 billion states — that's why the one-per-column encoding is used.

### Key performance numbers (memorize — classic quiz question)
| Method | Success rate | Avg. steps |
|---|---|---|
| Hill climbing (random start) | **~14 %** (stuck 86 %) | 4 when it succeeds, 3 when stuck |
| Hill climbing **+ sideways moves** (limit 100) | **~94 %** | 21 success, 64 failure |
| **Random-restart** hill climbing | **100 %** (eventually) | ≈ **7 restarts**, ≈ 22 steps total |

*Why ~7 restarts?* Expected restarts = 1/p = 1/0.14 ≈ 7. Total ≈ (6 failures × 3) + (1 success × 4) = **22 steps**.

---

## 3. Genetic Algorithm (FULL) ⭐⭐

A variant of **stochastic beam search** where successors come from **two parents** (sexual, not asexual, reproduction).

### The 5 ingredients
1. **Population** — k individuals (states), each encoded as a **string** over a finite alphabet
2. **Fitness function** — rates each individual (higher = better)
3. **Selection** — pick parents based on fitness
4. **Crossover (recombination)** — combine two parents into a child
5. **Mutation** — small random change, low probability

### 8-Queens encoding (the standard exam example)
- Individual = string of **8 digits, each 1–8** → e.g. `24748552`
- Digit *i* = **row of the queen in column *i***
- **Fitness = number of NON-attacking pairs**
- Maximum fitness = C(8,2) = **28** → fitness 28 means solved ✅

### Worked example (AIMA Fig. 4.6) — know this cold

**Initial population & selection probability** (fitness ÷ total, total = 24+23+20+11 = **78**):

| Individual | Fitness | Probability |
|---|---|---|
| 24748552 | 24 | 24/78 = **31 %** |
| 32752411 | 23 | 23/78 = **29 %** |
| 24415124 | 20 | 20/78 = **26 %** |
| 32543213 | 11 | 11/78 = **14 %** |

**Crossover** — parents `32752411` and `24748552`, crossover point after digit 3:
```
32752411  →  327 | 52411          Child 1: 327 + 48552 = 32748552
24748552  →  247 | 48552          Child 2: 247 + 52411 = 24752411
```

**Mutation** — flip one random digit, e.g. `32748552` → `32748152`.

### Pseudocode (AIMA)
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

### Why GA works — **schema** & building blocks
- A **schema** is a substring with some positions unspecified, e.g. `246*****`
- Instances of a schema that match = **building blocks**
- GA works best when **schemas correspond to meaningful components** of a solution
- Crossover's advantage: combines large blocks of letters that have evolved independently

---

## 4. SELECTION methods ⭐ (named topic — likely a direct question)

| Method | How it works | Note |
|---|---|---|
| **Roulette wheel** (fitness-proportionate) | P(i) = fᵢ / Σf — wheel slice ∝ fitness | Standard; a "super-individual" can dominate early |
| **Tournament** | Pick *k* at random, fittest of them wins | Simple, tunable pressure via *k* |
| **Rank** | Sort by fitness, select by **rank** not raw value | Fixes super-individual domination & scaling issues |
| **Elitism** | Copy the best *n* individuals straight to the next generation | Guarantees best solution is never lost |
| **Truncation** | Keep only the top x %, breed from those | Crude, fast |
| **SUS** (stochastic universal sampling) | One spin, evenly-spaced pointers | Lower variance than roulette wheel |

**Selection pressure:** too high → premature convergence (stuck in local optimum); too low → slow, near-random search.

---

## 5. Rapid-fire revision

- Local search keeps **one** state; GA keeps a **population**.
- GA = **stochastic beam search + crossover** (two parents).
- 8-queens fitness (GA) = **non-attacking pairs**, max **28**.
- 8-queens heuristic (hill climbing) = **attacking pairs**, goal **h = 0**.
- 8-queens successors = **56**; state space = **8⁸ ≈ 17 million**.
- Plain hill climbing solves 8-queens **~14 %**; with sideways moves **~94 %**.
- Random-restart expected restarts = **1/p ≈ 7**.
- Roulette-wheel probability = **fitness / total fitness**.
- Crossover point splits both parents; children swap the tails.
- Mutation rate is **low**; elitism protects the best individual.
- Simulated annealing accepts bad moves with prob **e^(ΔE/T)**, T decreasing.
