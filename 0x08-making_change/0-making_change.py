#!/usr/bin/python3
"""Making change problem Solution
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount
    using dynamic programming approach
    """
    if total <= 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[total] if dp[total] != total + 1 else -1
