class Solution:
    # def setZeroes(self, matrix):
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     zeros = list()
    #     for i in range(0, len(matrix)):
    #
    #         for j in range(0, len(matrix[i])):
    #
    #             if matrix[i][j] == 0:
    #                 zeros.append([i, j])
    #
    #     for zero in zeros:
    #         for i in range(len(matrix)):
    #             matrix[i][zero[1]] = 0
    #             for j in range(len(matrix[i])):
    #                 matrix[zero[0]][j] = 0
    def setZeroes(self, matrix):
        col = 1
        col_length = len(matrix[0])
        row_length = len(matrix)

        for i in range(0, row_length):
            if matrix[i][0] == 0:
                col = 0
            for j in range(1, col_length):

                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0


        for i in range(row_length - 1, -1, -1):

            for j in range(col_length - 1, 0, -1):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if col == 0:
                matrix[i][0] = 0

s = Solution()
matrix = [[1,1,2,0],[3,4,5,2],[1,3,1,5]]

s.setZeroes(matrix)

print(matrix)
