# kadane's algorithm
class Solution:
    def maxSubArray(self, nums):

        current_sum = 0
        maximum = nums[0]
        for value in nums:
            current_sum += value
            maximum = max(current_sum, maximum)
            if current_sum < 0:
                current_sum = 0

        return maximum
