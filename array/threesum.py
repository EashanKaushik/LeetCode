class Solution:
    def threeSum(self, nums):
        triplets = list()

        nums.sort()
        i = 0
        for i, curr in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            reqd_sum = -nums[i]
            while left < right:

                curr_sum = nums[left] + nums[right]

                if curr_sum > reqd_sum:
                    right -= 1
                elif curr_sum < reqd_sum:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return triplets


s = Solution()

# print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,0,0]))
