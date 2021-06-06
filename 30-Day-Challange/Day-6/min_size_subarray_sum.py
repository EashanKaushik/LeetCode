import sys

class Solution:
    def minSubArrayLen(self, target, nums):

        left = 0
        right = 0
        curr_sum = 0
        minimum = sys.maxsize
        found = False

        while right < len(nums):
            curr_sum += nums[right]

            while curr_sum >= target:
                sub_array_len = right - left + 1
                if minimum > sub_array_len:
                    minimum = sub_array_len
                    found = True
                curr_sum -= nums[left]
                left += 1

            right += 1

        return minimum if found else 0


s = Solution()

print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
