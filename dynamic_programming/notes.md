
---

# 🧠 What Is Dynamic Programming?

Dynamic Programming is a method for solving problems by breaking them down into overlapping subproblems, solving each subproblem once, and storing their solutions. There are two main approaches:

- **Top-down (memoization)**: recursion with caching
- **Bottom-up (tabulation)**: build a DP table iteratively (preferred method)

---

## 🔁 Patterns Mastered

### 1. **Climbing Stairs**
- You can climb either 1 or 2 steps.
- `dp[i] = dp[i-1] + dp[i-2]`
- Base cases: `dp[0] = 1`, `dp[1] = 1`
- Tabulation with space optimization possible.

---

### 2. **Min Cost Climbing Stairs**
- Cost to climb to the top, paying for step `i`
- `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`
- Base case: `dp[0] = 0`, `dp[1] = 0`

---

### 3. **Decode Ways (Leetcode 91)**
- DP based on single-digit or two-digit number rules (1–26)
- `dp[i] = dp[i-1] if s[i-1] != '0'`
- `dp[i] += dp[i-2] if 10 <= int(s[i-2:i]) <= 26`

---

### 4. **Longest Common Subsequence**
- 2D DP: `dp[i][j]` = LCS of first `i` chars of `text1` and `j` of `text2`
- Transition:
  - If match: `dp[i][j] = dp[i-1][j-1] + 1`
  - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

---

### 5. **Best Time to Buy and Sell Stock IV (at most k transactions)**
- 3D DP table: `dp[day][transactions_remaining][holding]`
- Transition:
  - If holding:
    - Sell or skip
    - `dp[i][t][1] = max(dp[i+1][t][1], prices[i] + dp[i+1][t-1][0])`
  - If not holding:
    - Buy or skip
    - `dp[i][t][0] = max(dp[i+1][t][0], -prices[i] + dp[i+1][t][1])`

---

### 6. **Transaction With Cooldown**
- State DP with three states:
  - `hold`: currently holding a stock
  - `sold`: just sold a stock today
  - `rest`: in cooldown or idle
- Transitions:
  ```python
  hold = max(prev_hold, prev_rest - price)
  sold = prev_hold + price
  rest = max(prev_rest, prev_sold)
  ```

---

### 7. **Stock with Transaction Fee**
- Similar to cooldown, but deduct fee only at sell:
  ```python
  hold = max(hold, cash - price)
  cash = max(cash, hold + price - fee)
  ```

---

## 🧱 Key Concepts You've Learned

- **Tabulation setup**: `dp = [0] * (n + 1)` or `[[0]*...]` to predefine state tables
- **1D DP**: fast and space efficient (`climbing stairs`)
- **2D DP**: LCS, grid problems
- **3D DP**: stock trading with constraints (transactions, cooldown, fee)
- **Stateful DP**: when action leads to a different constraint or restriction
- **Transitions**: Think about how each state leads to the next (buy/sell/skip/rest)
- **Base Cases**: Don’t overlook them — they anchor your whole recurrence

---

## 🧪 Meta-Style Readiness Tips

- Always explain:
  - State definition (`dp[i][j] = what?`)
  - Base cases
  - Recurrence logic
- Think aloud during interviews: walk through an example input
- Optimize space when asked
- Don't panic on 3D DP — focus on small transitions and build from there

---
