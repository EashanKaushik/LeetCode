class Solution:
    def canJump(self, nums):

        i = j = 0
        max_index = 0

        while i < len(nums)-1:

            if nums[i] == 0:

                if max_index < i + 1:
                    return False

            else:

                if i + nums[i] >= len(nums) - 1:
                    return True

            if i + nums[i] > max_index:
                max_index = i + nums[i]

            i += 1

        return True


s = Solution()
print(s.canJump([1,2,0,1,3,0,0,4]))
