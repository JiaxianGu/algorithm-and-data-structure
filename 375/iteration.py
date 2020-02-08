class Solution(object):
    l = 1
    r = n
    dp = [[0] * (n+1) for i in range(n+1)]
    for l in range(n-1, 0, -1):
        for r in range(l+1, n+1):
            mini = 999999999999
            for i in range(l, r):
                result = i+ max(dp[l][i-1], dp[i+1][r])
                if result < mini:
                    mini = result
            dp[l][r] = mini
    return dp[l][r]
