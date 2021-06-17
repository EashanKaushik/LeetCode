class Solution:
    def findPeakGrid(self, mat):

        row = 0

        while row < len(mat):


            left = 0
            right = len(mat[row]) - 1

            while left <= right:

                mid = left + (right - left)//2

                l = r = b = t = -1

                if mid == 0:
                    l = -1
                else:
                    l = mat[row][mid - 1]

                if mid == len(mat[row]) - 1:
                    r = -1
                else:
                    r = mat[row][mid + 1]

                if row == 0:
                    t = -1
                else:
                    t = mat[row-1][mid]

                if row == len(mat) - 1:
                    b = -1
                else:
                    b = mat[row + 1][mid]

                pivot = mat[row][mid]

                if pivot > l and pivot > r and pivot > b and pivot > t:
                    return [row, mid]

                if pivot < r:
                    left = mid + 1
                else:
                    right = mid - 1
            row += 1


s = Solution()
print(s.findPeakGrid([[1,4],[3,2]]))
