weights = [2, 3, 4, 5]
profits = [1, 2, 5, 6]
capacity = 8

n = len(weights)


dp = [[0 for _ in range(capacity + 1)]
      for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, capacity + 1):

        if weights[i - 1] <= j:

            dp[i][j] = max(
                profits[i - 1] + dp[i - 1][j - weights[i - 1]],
                dp[i - 1][j]
            )

        else:
           
            dp[i][j] = dp[i - 1][j]



print("DP Table:")

for row in dp:
    print(row)

print("Maximum Profit =", dp[n][capacity])
