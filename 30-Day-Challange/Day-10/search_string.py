class Solution:
    def exist(self, board, word):

        ans = False
        index = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:

                    temp = board[i][j]
                    board[i][j] = 'i'

                    if index == len(word) - 1:
                        return True

                    ans = self.soln(board, word, ans, i, j, index + 1)

                    board[i][j] = temp
                    if ans:
                        break

        return ans

    def soln(self, board, word, ans, i, j, index):

        # above
        if i - 1 >= 0 and not ans:
            if board[i - 1][j] == word[index]:
                temp = board[i - 1][j]
                board[i - 1][j] = ''
                if index == len(word) - 1:
                    return True

                ans = self.soln(board, word, ans, i-1, j, index + 1)
                board[i-1][j] = temp
        # left
        if j - 1 >= 0 and not ans:

            if board[i][j - 1] == word[index]:
                temp = board[i][j-1]
                board[i][j-1] = ''
                if index == len(word) - 1:
                    return True

                ans = self.soln(board, word, ans, i, j - 1, index + 1)
                board[i][j-1] = temp

        # right
        if j + 1 < len(board[0]) and not ans:

            if board[i][j + 1] == word[index]:
                temp = board[i][j + 1]
                board[i][j + 1] = ''
                if index == len(word) - 1:
                    return True

                ans = self.soln(board, word, ans, i, j + 1, index + 1)
                board[i][j + 1] = temp

        # buttom
        if i + 1 < len(board) and not ans:

            if board[i + 1][j] == word[index]:
                temp = board[i + 1][j]
                board[i + 1][j] = ''
                if index == len(word) - 1:
                    return True

                ans = self.soln(board, word, ans, i + 1, j , index + 1)
                board[i + 1][j] = temp

        return ans


s = Solution()

print(s.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
