class Solution:
    def spiralOrder(self, matrix):

        i = j = 0

        output = list()

        commands = {
            'right': (0, 1, 'down'),
            'down': (1, 0, 'left'),
            'left': (0 , -1, 'up'),
            'up': (-1, 0, 'right')
        }

        command = 'right'

        inc_i = 0
        inc_j = 1

        while 1:

            if i < 0 or j < 0 or i == len(matrix) or j == len(matrix[0]):
                break

            if matrix[i][j] == '*':
                break

            output.append(matrix[i][j])

            # print(matrix[i][j])

            matrix[i][j] = '*'

            # if going right
            if inc_j == 1:
                if j + 1 >= len(matrix[0]):
                    command = 'down'
                else:
                    if matrix[i][j+1] == '*':
                        command = 'down'

            # if going down
            elif inc_i == 1:
                if i + 1 >= len(matrix):
                    command = 'left'
                else:
                    if matrix[i+1][j] == '*':
                        command = 'left'

            # if going left
            elif inc_j == -1:
                if j - 1 < 0:
                    command = 'up'
                else:
                    if matrix[i][j-1] == '*':
                        command = 'up'

            # if going up
            elif inc_i == -1:
                if i - 1 < 0:
                    command = 'right'
                else:
                    if matrix[i-1][j] == '*':
                        command = 'right'


            inc_i, inc_j, next_command = commands[command]

            i += inc_i
            j += inc_j

        return output


s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
