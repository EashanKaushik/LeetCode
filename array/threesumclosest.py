class Solution:
    def threeSumClosest(self, nums, target):

        target_sum_min = None

        nums.sort()

        minimum = sys.maxsize

        for i in range(0, len(nums) - 1):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                target_sum = nums[i] + nums[left] + nums[right]

                if minimum > max(target, target_sum) - min(target_sum, target):

                    minimum = max(target, target_sum) - min(target_sum, target)
                    target_sum_min = target_sum

                if target_sum < target:
                    left += 1
                elif target_sum > target:
                    right -= 1
                else:
                    return target

        return target_sum_min

s = Solution()

print(s.threeSumClosest([-1,2,1,-4], 1))
