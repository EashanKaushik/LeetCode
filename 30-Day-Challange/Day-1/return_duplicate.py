class Solution:
    def findDuplicate1(self, nums):

        count = [0] * len(nums)

        for num in nums:
            count[num - 1] += 1
            if count[num - 1] > 1:
                return num

    def findDuplicate2(self, nums):

        i = nums[nums[0]] # slow
        j = nums[nums[nums[0]]] # fast

        while i != j:
            i = nums[i]
            j = nums[nums[j]]

        j = nums[0]

        while i != j:
            i = nums[i]
            j = nums[j]

        return i

    def findDuplicate3(self, nums):

        distinct = set()
        for num in nums:
            if num in distinct:
                return num
            else:
                distinct.add(num)

s = Solution()

print(s.findDuplicate2([1,3,4,2,2]))
