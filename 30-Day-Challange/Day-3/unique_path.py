class Solution:
    def uniquePaths(self, m, n):

        x, y = 1, 1
        dp = [[-1 for _ in range(0, n)] for _ in range(0, m)]

        return self.path(m, n, x, y, dp)


    def path(self, m, n, x, y, dp):

        if x > m or y > n:
            return 0

        if x == m and y == n:
            return 1

        if dp[x-1][y-1] != -1:
            return dp[x-1][y-1]

        r = self.path(m, n, x, y + 1, dp)
        b = self.path(m, n, x + 1, y, dp)

        dp[x-1][y-1] = r + b
        return dp[x-1][y-1]


s = Solution()

print(s.uniquePaths(3, 7))
