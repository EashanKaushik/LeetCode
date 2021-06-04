class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        count1 = 0
        count2 = 0

        element1 = None
        element2 = None

        for num in nums:

            if num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1
            elif count1 == 0:
                element1 = num
                count1 += 1
            elif count2 == 0:
                element2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for num in nums:
            if num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1

        output = set()

        if count1 > n//3:
            output.add(element1)
        if count2 > n//3:
            output.add(element2)

        return output

s = Solution()

print(s.majorityElement([2,2,1,1,1,2,2]))
