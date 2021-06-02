class Solution:
    def rotate(self, matrix):
        inner = outer = len(matrix)

        col = len(matrix) - 1

        temp = [[0 for _ in range(inner)] for _ in range(inner)]
        for i in range(0, outer):

            for j in range(0, inner):

                temp[j][col] = matrix[i][j]

            col -= 1

        for i in range(0, outer):

            for j in range(0, inner):

                matrix[i][j] = temp[i][j]

    def rotate2(self, matrix):

        n = len(matrix)

        for i in range(n):

            for j in range(i):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:

            low = 0
            high = n - 1

            while low < high:
                row[low], row[high] = row[high], row[low]

                low += 1
                high -= 1

s = Solution()

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

s.rotate2(matrix)

print(matrix)
