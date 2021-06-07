import sys

class Solution:
    def findLength(self, nums1, nums2):

        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        maximum = -1

        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    maximum = max(dp[i][j], maximum)

        return maximum if maximum != -1 else 0


s = Solution()

print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
