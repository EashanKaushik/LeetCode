class Solution:
    def searchMatrix(self, matrix, target):


        for row in matrix:
            row_max = row[-1]

            if target <= row_max:

                return self.binary_search(row, target)

    def binary_search(self, arr, target):

        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = low + (high - low) // 2

            if arr[mid] == target:
                return True

            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def searchMatrix2(self, matrix, target):

        m = len(matrix)
        n = len(matrix[0])

        pointer_row = 0

        pointer_col = n - 1

        while 0 <= pointer_row < m and 0 <= pointer_col < n:

            if matrix[pointer_row][pointer_col] == target:
                return True

            if matrix[pointer_row][pointer_col] < target:
                pointer_row += 1
            else:
                pointer_col -= 1

        return False

s = Solution()

print(s.searchMatrix2([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 61))
