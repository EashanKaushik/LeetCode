class Solution:
    def validPalindrome(self, s):

        left = 0
        right = len(s) - 1

        x = self.even(s, left, right)
        y = self.odd(s, left, right)

        return x or y

    def even(self, s, left, right):
        deleted = False
        while left < right:

            if s[left] != s[right]:
                if not deleted:
                    left += 1
                    deleted = True
                    continue
                else:
                    return False

            left += 1
            right -= 1

        return True

    def odd(self, s, left, right):
        deleted = False
        while left < right:

            if s[left] != s[right]:
                if not deleted:
                    right -= 1
                    deleted = True
                    continue
                else:
                    return False

            left += 1
            right -= 1

        return True


s = Solution()
                                            # 19                                                            81
print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
