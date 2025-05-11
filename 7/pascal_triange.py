def pascal_triange(n):
    dp = []
    for i in range(n):
        dp.append([1] * (i + 1))

    for i in range(2, n):
        for j in range(1, len(dp[i]) - 1):
            dp[i][j] += dp[i - 1][j - 1] + dp[i - 1][j] -1

    return dp


