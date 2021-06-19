class Solution:
    def numIslands(self, grid):

        count = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):

                if grid[row][col] == '1':
                    count += 1
                    self.count_island(grid, row, col)

        return count

    def count_island(self, grid, row, col):

        grid[row][col] = '2'

        if row - 1 >= 0  and grid[row-1][col] == '1':
            self.count_island(grid, row-1, col)

        if row + 1 < len(grid) and grid[row+1][col] == '1':
            self.count_island(grid, row+1, col)

        if col - 1 >= 0 and grid[row][col-1] == '1':
            self.count_island(grid, row, col-1)

        if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
            self.count_island(grid, row, col + 1)


s = Solution()
print(s.numIslands([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]))
