	“I’m using bottom-up dynamic programming with tabulation, so I initialize a dp array of size n + 1 where each dp[i] will store the minimum cost to reach step i.

	I start by setting all values to 0 using dp = [0] * (n + 1).

	Since we can start from step 0 or step 1, the cost to reach those positions is 0 — no steps have been taken yet. I’ll build up the solution by filling in the dp array starting from index 2 using the recurrence relation.”