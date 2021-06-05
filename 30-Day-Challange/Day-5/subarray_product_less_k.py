class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if (k <= 1):
            return 0

        product = 1
        left = 0
        right = 0
        result = 0

        while(right < len(nums)):

            product *= nums[right]

            while(product >= k):
                product /= nums[left]
                left += 1

            result += right - left + 1

            right += 1

        return result

s = Solution()

print(s.numSubarrayProductLessThanK([10,5,2,6], 100))
