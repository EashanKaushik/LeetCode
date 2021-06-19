import sys

class Solution:
    def maxAreaOfIsland(self, grid):

        count = 0
        max_area = -sys.maxsize - 1

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):

                if grid[row][col] == 1:
                    area = self.count_island(grid, row, col)

                    if area > max_area:
                        max_area = area

        return max_area if max_area > 0 else 0

    def count_island(self, grid, row, col, count = 0):

        count += 1

        grid[row][col] = 2

        if row - 1 >= 0  and grid[row-1][col] == 1:
            count = self.count_island(grid, row-1, col, count)

        if row + 1 < len(grid) and grid[row+1][col] == 1:
            count = self.count_island(grid, row+1, col, count)

        if col - 1 >= 0 and grid[row][col-1] == 1:
            count = self.count_island(grid, row, col-1, count)

        if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
            count = self.count_island(grid, row, col + 1, count)

        return count



s = Solution()
print(s.maxAreaOfIsland([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]))
