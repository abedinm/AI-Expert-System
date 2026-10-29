# CSC4226 — Observation Worksheet Answers

Student name: Minhazul Abedin  ID: 21-44625-1  Section: W

---

## Page 1 — Notebook 1: Introduction to AI

| # | Answer |
|---|--------|
| 1 | **Think Rationally** and **Act Rationally**. |
| 2 | **Think Humanly**. |
| 3 | **Vision Robot**, with a Robotics score of **5**. |
| 4 | **Computer vision** and **Robotics**. Both are 0. |
| 5 | **Integrated Agent**. Its gap is **0**: every score is 4, so max − min = 4 − 4. |
| 6 | **Integrated Agent**, with an average of **4.00**. Vision Robot is 3.67 and Text Assistant is 2.83. |
| 7 | **Inception of AI**, starting in **1943**. |
| 8 | **Big data** (2001) and **Deep learning** (2011). |
| 9 | **HMM** and **Bayesian Network**. |
| 10 | **8**: Philosophy, Mathematics, Economics, Neuroscience, Psychology, Computer engineering, Control theory and cybernetics, and Linguistics. |
| 11 | There is a three-way tie at 2 each: **Engineering**, **Behavior/Biology** and **Formal/Quantitative**. |
| 12 | A complete Turing Test needs all six capabilities. The Integrated Agent scores 4 on every one, so it has the highest average (4.00) and a specialization gap of 0. The specialized systems have weak spots. Text Assistant scores 0 in vision and robotics, so its gap is 5. Vision Robot scores only 2 in natural language, so its gap is 3. Being balanced across all capabilities matters more than being excellent at one. |

## Page 2 — Notebook 2: Intelligent Agents

| # | Answer |
|---|--------|
| 1 | **8** possible states: 2 locations × 2 × 2 dirt states. |
| 2 | The letter is the **agent's current location**. The first bit is **whether A is dirty** and the second is **whether B is dirty** (1 = dirty, 0 = clean). In A\|10 the agent is in A, A is dirty and B is clean. |
| 3 | **12** directed transitions that change the state. |
| 4 | **Suck → Right → Suck**. |
| 5 | **Step 3**, at state (B, 0, 0). |
| 6 | **Clean**. |
| 7 | **2**: Left and Right. ("Dirty" maps only to Suck.) |
| 8 | **Chess with a clock** and **Image analysis**. |
| 9 | **Taxi driving**, with a count of 6. That is all six challenging categories. |
| 10 | **Image analysis** and **Part-picking robot**. |
| 11 | Under Speed priority: **Balanced Route** (8.25, just ahead of Fast Highway at 8.15). Under Safety priority: **Balanced Route** (8.65, ahead of Scenic Route at 8.55). |
| 12 | All three routes reach the destination. A goal-based agent only checks "goal reached: yes/no", so it sees all three as equally good. A utility-based agent scores each route by weighting time, safety and cost, so it can rank routes that all succeed. When the weights change, the rankings change too. Under Speed priority, Fast Highway (8.15) is a close second. Under Safety priority, Scenic Route (8.55) is second and Fast Highway drops to last (6.15). With these scores, Balanced Route has the highest utility under every preference, because it does well on all three criteria. |

## Page 3 — Notebook 3: Uninformed Search

| # | Answer |
|---|--------|
| 1 | **20** states (cities) and **23** roads. |
| 2 | **Arad → Sibiu → Fagaras → Bucharest**, with cost **450** (140 + 99 + 211). |
| 3 | **Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest**, with cost **418** (140 + 80 + 97 + 101). |
| 4 | **No.** BFS's route costs 450 but UCS's route costs 418, so a route that is 32 cheaper exists. BFS finds the route with the fewest edges (depth 3), which is not the cheapest one. |
| 5 | **Arad → Sibiu → Fagaras → Bucharest**, with cost 450. |
| 6 | **DFS**, with 4 nodes expanded. BFS expands 9, UCS 13 and IDS 18. |
| 7 | **UCS**, with a maximum frontier of 4. BFS, DFS and IDS each reach 5. |
| 8 | **Sibiu** for BFS, and **Sibiu** for DFS as well. |
| 9 | **Depth limit 3**. |
| 10 | It expands **9** nodes and does **not** find the goal. |
| 11 | It finds the goal at **limit 3**, returning **Arad → Sibiu → Fagaras → Bucharest** (cost 450, 18 total expansions). |
| 12 | BFS stops at the goal with the fewest edges, so it ignores edge costs. Its 3-edge route uses the expensive Fagaras–Bucharest road (211), for a total of 140 + 99 + 211 = **450**. UCS always expands the cheapest path cost first. It goes through Rimnicu Vilcea (80) and Pitesti (97, then 101) instead. That route has 4 edges but each edge is cheaper: 140 + 80 + 97 + 101 = **418**. In a weighted graph, the shallowest route is not necessarily the cheapest one. |
