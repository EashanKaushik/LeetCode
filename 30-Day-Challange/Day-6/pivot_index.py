class Solution:
    def pivotIndex(self, nums):

        left = 0
        right = 0

        left_sum = 0
        right_sum = sum(nums)

        while right < len(nums):

            right_sum -= nums[right]
            right += 1

            if right_sum == left_sum:
                return left
            else:
                left_sum += nums[left]
                left += 1

        return -1
