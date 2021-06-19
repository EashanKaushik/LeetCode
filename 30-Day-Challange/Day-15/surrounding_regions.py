class Solution:
    def solve(self, board):
        for row in range(0, len(board)):

            if board[row][0] == 'O': self.check_border_connect(board, row, 0)

            if board[row][len(board[0]) - 1] == 'O': self.check_border_connect(board, row, len(board[0]) - 1)

        for col in range(0, len(board[0])):

            if board[0][col] == 'O': self.check_border_connect(board, 0, col)

            if board[len(board) - 1][col] == 'O': self.check_border_connect(board, len(board) -1, col)

        for row in range(0, len(board)):

            for col in range(0, len(board[0])):

                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '*':
                    board[row][col] = 'O'

    def check_border_connect(self, board, row, col):

        if board[row][col] == 'O':
            board[row][col] = '*'

        if row - 1 >= 0 and board[row-1][col] == 'O':self.check_border_connect(board, row - 1, col)

        if row + 1 < len(board) and board[row + 1][col] == 'O': self.check_border_connect(board, row + 1, col)

        if col - 1 >= 0 and board[row][col-1] == 'O': self.check_border_connect(board, row, col-1)

        if col + 1 < len(board[0]) and board[row][col+1] == 'O': self.check_border_connect(board, row, col+1)


s = Solution()
print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
