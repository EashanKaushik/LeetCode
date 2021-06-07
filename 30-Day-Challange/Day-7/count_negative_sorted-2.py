class Solution:
    def countNegatives(self, grid):

        m = len(grid)
        n = len(grid[0])

        current = 0
        row = 0
        col = n - 1

        while row < m and col >= 0:

            curr = grid[row][col]

            if curr < 0:
                current += m - row
                col -= 1
            else:
                row += 1

        return current


s = Solution()

print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
