class Solution:
    def fourSum(self, nums, target):

        quad = []

        nums.sort()

        for i in range(0, len(nums) - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i+1, len(nums) - 2):

                if j > (i + 1) and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:

                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum < target:
                        left += 1
                    elif curr_sum > target:
                        right -= 1
                    else:
                        quad.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return quad

s = Solution()

print(s.fourSum([1,0,-1,0,-2,2], 0))
