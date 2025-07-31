def coinChange(coins, amount):
    n = len(coins)
    dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

    # Base case: amount 0 requires 0 coins
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                # Include current coin (i-1) or exclude it
                dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
            else:
                # Can't include current coin
                dp[i][j] = dp[i - 1][j]

    result = dp[n][amount]
    return result if result != float('inf') else -1
    
    
print(coinChange([1, 3, 4], 6))  
