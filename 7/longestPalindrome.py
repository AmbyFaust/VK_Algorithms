def longestPalindrome(s):
    if len(s) <= 1:
        return s
    dp = [[None] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True

    pos = (0, 0)
    for delta in range(1, len(s)):
        for i in range(len(s)):
            j = i + delta
            if j >= len(s):
                break
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i > pos[1] - pos[0]:
                    pos = (i, j)
            else:
                dp[i][j] = False

    return s[pos[0]:pos[1] + 1]

