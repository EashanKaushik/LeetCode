class Solution:
    def isPalindrome(self, s):
        if len(s) == 1:
            return True
        s = [strs for strs in s.lower() if strs.isalnum()]

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


s = Solution()
print(s.isPalindrome('0P'))
