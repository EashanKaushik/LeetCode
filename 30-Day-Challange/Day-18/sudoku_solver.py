class Solution:
    def isValidSudoku(self, board):

        already_seen = set()

        for row in range(0, len(board)):

            for col in range(0, len(board[row])):

                if board[row][col] != '.':
                    row_val = f'{board[row][col]} at row {row}'
                    col_val = f'{board[row][col]} at col {col}'
                    box_val = f'{board[row][col]} at box {row//3} {col//3}'

                    print(row_val, col_val, box_val)

                    print(already_seen)

                    if row_val in already_seen or col_val in already_seen or box_val in already_seen:
                        return False

                    already_seen.add(row_val)
                    already_seen.add(col_val)
                    already_seen.add(box_val)

        return True


s = Solution()
print(s.isValidSudoku(
                    [["8","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]]
                    ))
