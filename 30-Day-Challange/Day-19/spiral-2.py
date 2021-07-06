class Solution:
    def generateMatrix(self, n):

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        commands = {
            'right': (0, 1),
            'down': (1, 0),
            'left': (0, -1),
            'up': (-1, 0)
        }

        i = j = 0
        command = 'right'
        inc_i, inc_j = 0, 1
        curr_n = 1

        while 1:

            if i < 0 or j < 0 or i == n or j == n:
                break

            if matrix[i][j] != 0:
                break

            matrix[i][j] = curr_n

            curr_n += 1

            if inc_j == 1:

                if j + 1 >= n:
                    command = 'down'
                else:

                    if matrix[i][j+1] != 0:
                        command = 'down'
            elif inc_i == 1:

                if i + 1 >= n:
                    command ='left'
                else:

                    if matrix[i+1][j] != 0:
                        command = 'left'
            elif inc_j == -1:

                if j - 1 < 0:
                    command = 'up'
                else:
                    if matrix[i][j-1] != 0:
                        command = 'up'
            elif inc_i == -1:

                if i - 1 < 0:
                    command = 'right'
                else:
                    if matrix[i-1][j] != 0:
                        command = 'right'

            inc_i, inc_j = commands[command]

            i += inc_i
            j += inc_j

        return matrix


s = Solution()
print(s.spiralOrder(3)
