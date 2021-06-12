class Solution:
    def generateParenthesis(self, limit):

        total_open = 1
        current_open = 1
        ans = []

        current = ["("]
        self.generate(ans, total_open, current_open, limit, current)

        return ans

    def generate(self, ans, total_open, current_open, limit, current):

        if total_open == limit:
            if current_open > 0:
                current.append(")")
                self.generate(ans, total_open, current_open - 1, limit, current)
                current.pop()
            else:
                ans.append(''.join(current))
            return


        current.append("(")
        self.generate(ans, total_open + 1, current_open + 1, limit, current)
        current.pop()

        if current_open > 0:
            current.append(")")
            self.generate(ans, total_open, current_open - 1, limit, current)
            current.pop()

s = Solution()

print(s.generateParenthesis(3))
