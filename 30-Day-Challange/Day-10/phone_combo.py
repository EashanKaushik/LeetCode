class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []
        digit_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        ans = list()
        curr = list()
        self.soln(digits, ans, curr, 0, digit_map)

        return ans

    def soln(self, digits, ans, curr, index, digit_map):
        if index > len(digits):
            return

        if len(curr) == len(digits):
            ans.append(''.join(curr))
            return

        if index < len(digits):

            alphas = digit_map[int(digits[index])]
            for alpha in alphas:
                curr.append(alpha)
                self.soln(digits, ans, curr, index + 1, digit_map)
                curr.pop()


s = Solution()

print(s.letterCombinations('22'))
