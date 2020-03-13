class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for i in range(n+1)]
        return self.solve(dp, 1, n)
    
    def solve(self, dp, l, r):
        if l >= r:
            return 0
        if dp[l][r]:
            return dp[l][r]
        mini = 9999999999
        for i in range(l, r+1):
            result = i + max(self.solve(dp, l, i-1), self.solve(dp, i+1, r))
            if result < mini:
                mini = result
        dp[l][r] = mini
        return dp[l][r]