# Final Term Study Plan — Artificial Intelligence and Expert System (CSC4226)
Minhazul Abedin · 21-44625-1 · Section C

> **Where this scope comes from:** the AIUB *"Artificial Intelligence & Expert System Final Term"*
> review video, which walks the exam topics in order. It is not an official syllabus — if your
> instructor posts one, check it against this and adjust.

---

## The scope, in exam order

| # | Topic | Video time | Status |
|---|---|---|---|
| 1 | Alpha-Beta Pruning | ~00:00 | new |
| 2 | Genetic Algorithm | ~13:25 | ✅ done for the quiz |
| 3 | 8-Queen Problem | ~28:15 | ✅ done for the quiz |
| 4 | Constraint Satisfaction (CSP) | ~40:00 | new |
| 5 | Bayesian Networks | ~65:10 | new |

**Two of five are already in your pocket.** Topics 2 and 3 are covered in
`QUIZ-PREP-complete.md` with verified worked examples. The real work is 1, 4 and 5.

---

# TOPIC 1 — Alpha-Beta Pruning

Adversarial search: two players, MAX wants the highest value, MIN wants the lowest.
Alpha-beta gives the **same answer as minimax** but skips branches that cannot change it.

## The two values
- **α (alpha)** — the best value MAX can guarantee so far. Starts at **−∞**. Only MAX updates it.
- **β (beta)** — the best value MIN can guarantee so far. Starts at **+∞**. Only MIN updates it.

## The rules
1. Search **left to right, depth first**.
2. Values travel **child → parent**. α/β travel **parent → child**.
3. **Prune when α ≥ β.** Stop examining the rest of that node's children.

## Worked example (verified)
Root is MAX, three MIN children, leaves left to right:

```
            MAX
      /      |      \
    MIN     MIN     MIN
   / | \   / | \   / | \
  3 12  8 2  4  6 14 5  2
```

**Trace**
- MIN₁ sees 3, 12, 8 → returns **3**. Root α = 3.
- MIN₂ sees 2. Now 2 ≤ α(3), so MIN₂ can only get worse for MAX → **prune 4 and 6**.
- MIN₃ sees 14, 5, 2 → returns **2**.
- Root = max(3, 2, 2) = **3**

| Result | Value |
|---|---|
| Minimax value | **3** |
| Alpha-beta value | **3** (always identical) |
| Leaves examined | 3, 12, 8, 2, 14, 5, 2 → **7 of 9** |
| Leaves pruned | **4 and 6** |

## Exam checklist
- [ ] α = −∞, β = +∞ at the start
- [ ] MAX updates α, MIN updates β
- [ ] Prune condition: **α ≥ β**
- [ ] Alpha-beta never changes the answer, only the work
- [ ] Best case ordering examines **O(b^(m/2))** — effectively doubles the searchable depth

---

# TOPIC 2 — Genetic Algorithm  *(already covered)*

See `QUIZ-PREP-complete.md`. Key items to re-skim the night before:

- GA = **stochastic beam search + two parents**
- Cycle: Initialize → Fitness → **Selection → Crossover → Mutation → Survival**
- **Roulette wheel:** P(i) = fitnessᵢ ÷ Σ fitness, then cumulative bins
- **Best selection:** just take the top N by fitness, no randomness
- Six crossovers: one-point, two-point, uniform, arithmetic, heuristic, **three-parent**
  (three-parent rule: P1 == P2 → take P1, else take P3)
- Worked example: f(x) = x²/2 − 3x, 5-bit binary, **negative fitness clamped to 0**

**Your own lab code is revision material** — `Lab-Crossover-NQueens/problem1_crossover.py`
is single-point crossover, and the 12-bit example from the lab sheet reproduces exactly.

---

# TOPIC 3 — 8-Queens  *(already covered)*

See `QUIZ-PREP-complete.md`. The essentials:

- Chromosome = 8 digits, digit *i* = **row of the queen in column *i***
- **Fitness = non-attacking pairs**, max = n(n−1)/2 → **28** for 8 queens, **15** for 6
- Attack test: **same row** OR **|Δrow| == |Δcol|**
- `24748552` → 4 attacks → **fitness 24**; the four AIMA states are 24, 23, 20, 11 (total 78)
- The **shortcut trick**: per digit scan right — duplicate / count up / count down

**Your lab code covers this too** — `problem2_nqueen_attack.py` implements the three attack
types with `abs(j - l) == abs(k - i)`.

---

# TOPIC 4 — Constraint Satisfaction Problems (CSP)

## The three components
| Component | Meaning | Map-colouring example |
|---|---|---|
| **Variables** | what must be assigned | WA, NT, SA, Q, NSW, V, T |
| **Domains** | allowed values | {Red, Green, Blue} |
| **Constraints** | what is forbidden | adjacent regions differ |

A **solution** is a complete, consistent assignment.

## Constraint graph
One node per variable; an edge between any two variables sharing a constraint.
Australia's degrees (verified):

| Variable | Neighbours | Degree |
|---|---|---|
| **SA** | WA, NT, Q, NSW, V | **5** ← most constrained |
| NT | WA, SA, Q | 3 |
| Q | NT, SA, NSW | 3 |
| NSW | SA, Q, V | 3 |
| WA | NT, SA | 2 |
| V | SA, NSW | 2 |
| T | — | 0 (island, unconstrained) |

## Forward Checking
After each assignment, delete that value from the domains of all neighbours.
If any domain becomes **empty → backtrack immediately**.

**Verified trace:**

After `WA = Red`:
```
NT  {G, B}      SA  {G, B}      Q {R,G,B}   NSW {R,G,B}   V {R,G,B}   T {R,G,B}
```

After `WA = Red, NT = Green`:
```
SA  {B}         Q  {R, B}       NSW {R,G,B}   V {R,G,B}   T {R,G,B}
```
SA is down to a single value.

## The two heuristics — do not mix them up

**MRV — Minimum Remaining Values** ("most constrained variable")
> Choose the variable with the **fewest legal values left**.
> In the trace above → **SA**, domain size 1.
> Fails fastest, so it prunes the search early.

**Degree heuristic** ("most constraining variable")
> Choose the variable involved in the **most constraints on unassigned variables**.
> Used as a **tie-breaker** when MRV gives a draw.
> At the start, all domains are size 3 → tie → degree picks **SA** (5 neighbours).

⚠️ **MRV counts values left. Degree counts neighbours.** That's the distinction they test.

## Exam checklist
- [ ] Define variables, domains, constraints for a given problem
- [ ] Draw the constraint graph
- [ ] Run forward checking and show the shrinking domains
- [ ] Apply MRV; use degree to break ties
- [ ] Empty domain ⇒ backtrack

---

# TOPIC 5 — Bayesian Networks

A directed acyclic graph. Each node is a variable; each edge means "directly depends on".
Every node carries a table of **P(node | its parents)**.

## The rules you need
1. **Complement:** `P(¬X) = 1 − P(X)`
2. **Chain rule:** the full joint = product of every node given its parents
3. **Root nodes** (no parents) just use their prior
4. **Marginalisation:** if a variable isn't mentioned in the query, **sum over both its values**
5. **Normalisation:** P(X | e) = P(X, e) ÷ P(e), where P(e) sums over all values of X

## Standard network (burglary / earthquake / alarm)
```
   Burglary        Earthquake
        \             /
         \           /
            Alarm
           /     \
    JohnCalls   MaryCalls
```
P(B)=0.001 · P(E)=0.002
P(A|B,E)=0.95 · P(A|B,¬E)=0.94 · P(A|¬B,E)=0.29 · P(A|¬B,¬E)=0.001
P(J|A)=0.90 · P(J|¬A)=0.05 · P(M|A)=0.70 · P(M|¬A)=0.01

## Worked example (verified)
**"Alarm sounds, both call, but no burglary and no earthquake."**

```
P(j, m, a, ¬b, ¬e)
 = P(¬b) × P(¬e) × P(a|¬b,¬e) × P(j|a) × P(m|a)
 = 0.999 × 0.998 × 0.001 × 0.90 × 0.70
 = 0.000628
```

Note the order: **follow the arrows down the graph.** Parents before children, every time.

**Sanity checks I ran:** the full joint over all 32 combinations sums to exactly 1, and
`P(B | j, m) = 0.284`, which matches the textbook value.

## Exam checklist
- [ ] Read dependencies off the graph (who are the parents?)
- [ ] Write a joint probability as a product, parents first
- [ ] `P(¬X) = 1 − P(X)` for every negative term
- [ ] Sum over a variable that the question does not fix
- [ ] Normalise when asked for a conditional

---

# Supporting material (cheap marks, learn if time allows)

**Local search** — from Lecture 4:
- Hill climbing gets stuck on **local maxima, ridges, plateaux**
- Variants: steepest-ascent · stochastic · first-choice · **random-restart**
- **Simulated annealing:** accept a bad move if `random < e^(ΔE/T)`; uphill always accepted
- **Local beam search** keeps *k* states; stochastic beam is GA's ancestor

**Agents** — from Lecture 2:
- **PEAS** = Performance, Environment, Actuators, Sensors
- Environment properties: observable · deterministic · episodic · static · discrete · single-agent
- Agent types: simple reflex → model-based → goal-based → utility-based → learning
- Your two lab programs are one of each: water purification = **goal-based**, vacuum = **simple reflex**

---

# The schedule

Adjust the dates to your exam. This assumes **6 days**.

### Day 1 — Alpha-Beta (2h)
Learn α/β, the pruning condition, and trace the 3/12/8 · 2/4/6 · 14/5/2 tree by hand until you
get 7 leaves examined and 4, 6 pruned without looking. Then invent your own tree and trace it.

### Day 2 — CSP part one (2h)
Variables/domains/constraints. Draw Australia's constraint graph from memory. Run forward
checking after WA=Red, then WA=Red + NT=Green, and check your domains against this file.

### Day 3 — CSP part two (1.5h)
MRV vs degree until the difference is automatic. Do a full colouring of Australia with forward
checking, writing the domains at every step.

### Day 4 — Bayesian Networks (2.5h)
Draw the burglary network with all its tables. Compute `P(j, m, a, ¬b, ¬e)` by hand → expect
0.000628. Then do a query needing marginalisation, and one needing normalisation.

### Day 5 — Revision of GA + 8-Queens (2h)
`QUIZ-PREP-complete.md` and the practice problems at the end. You have already been examined on
this, so keep it to a refresh — the shortcut trick, roulette wheel, the f(x) cycle.

### Day 6 — Mixed practice (2h)
One problem from each of the five topics, no notes. Whatever you fumble, that is your morning
revision.

### Exam morning (30 min)
Formulas only:
```
prune when  α ≥ β
fitness     = n(n-1)/2 − attacks
roulette    P(i) = fᵢ / Σf
MRV         fewest values left      degree = most neighbours
joint       ∏ P(node | parents)     P(¬X) = 1 − P(X)
annealing   accept bad move if random < e^(ΔE/T)
```

---

# What you already have

| Resource | Location |
|---|---|
| GA + 8-Queens guide, verified, with practice problems | `QUIZ-PREP-complete.md` |
| Animated explainer (109 s) | `~/Desktop/8Queens-GA-explainer.mp4` |
| Narrated revision video + podcast | `~/Desktop/AI-Quiz-Prep/` |
| Lecture PDFs 1–5 + final-term video | NotebookLM notebook "AI Quiz — GA & Local Search" |
| Your own lab code (crossover, N-queens, both agents) | `~/Developer/AI-Expert-System/` |

**Biggest risk:** leaving CSP and Bayesian Networks until the last two days. They are the two
topics you have never been examined on, and Bayesian Networks is the most calculation-heavy
thing on the paper. Start there if you get short on time.
