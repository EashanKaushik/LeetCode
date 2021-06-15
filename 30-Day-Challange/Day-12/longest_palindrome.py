class Solution:
    def longestPalindrome(self, s):

        if not s:
            return

        index = 0
        maximum = 0
        curr = str()

        while index < len(s):

            left, right = index, index

            maximum, curr = self.check(s, left, right, maximum, curr)

            maximum, curr = self.check(s, left, right + 1, maximum, curr)

            index += 1

        return curr

    def check(self, s, left, right, maximum, curr):

        while left >= 0 and right < len(s) and s[left] == s[right]:

            sub_string = s[left: right + 1]

            if len(sub_string) > maximum:
                maximum = len(sub_string)
                curr = sub_string

            left -= 1
            right += 1

        return maximum, curr


s = Solution()

print(s.longestPalindrome("bababb"))
