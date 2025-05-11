import numpy as np


def coinChange(coins, amount):
    dp = [np.inf] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == np.inf:
        return -1
    return dp[amount]



