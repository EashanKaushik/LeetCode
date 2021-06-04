class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) / 2
        actual_sum = 0
        for num in nums:
            actual_sum += num

        return int(expected_sum - actual_sum)


s = Solution()

print(s.missingNumber([0, 3, 1]))
