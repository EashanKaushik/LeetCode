class Solution:
    def twoSum(self, numbers, target):

        first = 0
        last = len(numbers) - 1

        while first < last:
            curr_sum = numbers[first] + numbers[last]

            if curr_sum < target:
                first += 1
            elif curr_sum > target:
                last -= 1
            else:
                return [first + 1, last + 1]


s = Solution()
print(s.twoSum([2,7,11,15], 9))
