def coin_change(coins, amount):
    # Create DP table
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    # Calculate minimum coins for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# Coins available
coins = [1, 2, 5]

# Amount to make
amount = 11

# Find minimum number of coins
result = coin_change(coins, amount)

print("Minimum number of coins:", result)
