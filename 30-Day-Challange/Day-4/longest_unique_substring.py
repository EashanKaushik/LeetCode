class Solution:
    def lengthOfLongestSubstring(self, s):

        unique = {}
        left = 0
        right = 0

        while left <= right and right < len(s):

            if s[right] not in unique:
                unique[s[right]] =  right
                right += 1
            else:
                left = unique[s[right]] + 1
                unique[s[right]] = right
                right = left + 1

        return len(unique)


s = Solution()

print(s.lengthOfLongestSubstring("bbba"))
