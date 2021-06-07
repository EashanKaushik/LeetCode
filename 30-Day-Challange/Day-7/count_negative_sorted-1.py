class Solution:
    def countNegatives(self, grid):

        m = len(grid)
        n = len(grid[0])

        index = 0
        count = 0

        while index < m:

            count += (n - self.binary_search(grid[index]))

            index += 1

        return count

    def binary_search(self, nums):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left)// 2

            if nums[mid] >= 0 :
                left = mid + 1
            else:
                right = mid - 1

        return left


s = Solution()

print(s.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
