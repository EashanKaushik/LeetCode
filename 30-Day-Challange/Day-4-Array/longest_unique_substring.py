class Solution:
    def lengthOfLongestSubstring(self, s):

        unique = set()
        left = 0
        right = 0
        maxi = 0

        while right < len(s):

            if s[right] not in unique:
                unique.add(s[right])
                right+=1
                maxi = max(maxi, len(unique))
            else:
                unique.discard(s[left])
                left += 1
        return maxi


s = Solution()

print(s.lengthOfLongestSubstring("bbba"))
