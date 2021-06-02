class Solution:
    def majorityElement(self, nums):

        nums.sort()

        return nums[len(nums)//2]

    def majorityElement2(self, nums):

        count = 0
        element = 0

        for num in nums:
            if count == 0:
                element = num

            if num == element:
                count += 1
            else:
                count -= 1

        return element

    def majorityElement3(self, nums):

        return max(set(nums), key=nums.count)

s = Solution()

print(s.majorityElement2([2,2,1,1,1,2,2]))
