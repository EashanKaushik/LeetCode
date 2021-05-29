class Solution:
    def removeDuplicates(self, nums):

        swap = i = 1

        while(i < len(nums)):

            if nums[i] != nums[i-1]:
                nums[swap] = nums[i]
                i += 1
                swap += 1
            else:
                i+= 1

        return swap

s = Solution()

return(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
