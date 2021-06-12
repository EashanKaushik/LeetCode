class Solution:
    def partition(self, s):
        if not s:
            return []

        curr = list()
        ans = list()
        dp = set()

        self.divide(s, curr, ans, dp)

        return ans

    def divide(self, s, current, ans, dp):

        if len(s) == 0:
            ans.append(current.copy())

        for i in range(1, len(s) + 1):
            if self.palindrome(s[:i], dp):
                current.append(s[:i])
                self.divide(s[i:], current, ans, dp)
                current.pop()

    def palindrome(self, word, dp):

        is_palindrome = True

        if word in dp:
            return is_palindrome

        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                is_palindrome = False
                break

            left += 1
            right -= 1

        if is_palindrome:
            dp.add(word)

        return is_palindrome


s = Solution()

print(s.partition('abbab'))
