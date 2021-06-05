class Solution:
    def subarraySum(self, nums, k):

        if len(nums) == 1:
            if nums[0] == k:
                return 1
            return 0

        # nums.sort()

        left = 0
        right = 0
        curr_sum = 0
        count = 0
        while(right < len(nums)):
            curr_sum += nums[right]

            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == k:
                count += 1

            right += 1

        # print(curr_sum)

        while left < right - 1:
            curr_sum -= nums[left]
            # print(curr_sum)

            if curr_sum == k:
                count += 1

            left += 1
        return count




s = Solution()

print(s.subarraySum([-1, -1, 1], 0))
