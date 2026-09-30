# AI-Expert-System

Coursework for **CSC4226 — Artificial Intelligence and Expert System** (AIUB).

## Structure

```
LabTask-1/              Python intro problems
LabTask-2/              Data structures, list processing, matrix multiplication
Lab-Crossover-NQueens/  Genetic algorithm crossover + N-Queens attack detection
Final-Lab-Task/         Intelligent agents (water purification, vacuum cleaner)
notes/                  Quiz and final-term study notes
```

## Labs

### LabTask-1 — Python basics

| File | Description |
|------|-------------|
| [`q1_month_name.py`](LabTask-1/q1_month_name.py) | Month name from number using `match`-`case` |
| [`q2_factorial.py`](LabTask-1/q2_factorial.py) | Factorial of a number |
| [`q3_largest_element.py`](LabTask-1/q3_largest_element.py) | Largest element in a list |
| [`q4_leap_year.py`](LabTask-1/q4_leap_year.py) | Leap year check |
| [`q5_multiplication_table.py`](LabTask-1/q5_multiplication_table.py) | Multiplication table |

### LabTask-2 — Set, Tuple, Dictionary, matrices

| File | Description |
|------|-------------|
| [`task1.py`](LabTask-2/task1.py) | Takes integers, removes duplicates, sorts descending, filters out multiples of 3 |
| [`task2.py`](LabTask-2/task2.py) | Matrix multiplication of two 2D matrices using nested loops |
| [`study-material.md`](LabTask-2/study-material.md) | Study notes: Set, Tuple, Dictionary + concepts behind both tasks |
| [`cheatsheet.md`](LabTask-2/cheatsheet.md) | One-page quick reference |

### Crossover & N-Queens

| File | Description |
|------|-------------|
| [`problem1_crossover.py`](Lab-Crossover-NQueens/problem1_crossover.py) | Single-point crossover (genetic algorithm) |
| [`problem2_nqueen_attack.py`](Lab-Crossover-NQueens/problem2_nqueen_attack.py) | Detects attacking queen pairs on an N×N board |

### Final Lab Task — Agents

| File | Description |
|------|-------------|
| [`task1_water_purification.py`](Final-Lab-Task/task1_water_purification.py) | Water purification agent |
| [`task2_vacuum_agent.py`](Final-Lab-Task/task2_vacuum_agent.py) | Vacuum cleaning agent on a 4×4 grid |

## Notes

- [Quiz prep — GA & 8-Queens](notes/quiz-prep-ga-8queens.md) · [complete guide](notes/quiz-prep-complete.md)
- [Final term — complete guide](notes/final-term-complete.md) · [study plan](notes/final-term-study-plan.md) · [practice problems](notes/final-term-practice-problems.md)

## Running

Python 3.10+ (for `match`-`case`). No dependencies.

```bash
python3 LabTask-1/q1_month_name.py
python3 LabTask-2/task1.py     # then type integers, e.g. 9 3 3 7 12 5 8 6 10
python3 Final-Lab-Task/task2_vacuum_agent.py
```
