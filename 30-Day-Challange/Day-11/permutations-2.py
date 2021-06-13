from collections import Counter

class Solution:
    def permuteUnique(self, nums):
        ans = list()
        curr = list()
        count = Counter(nums)
        self.permutations(nums, curr, ans, count)

        return ans

    def permutations(self, nums, curr, ans, count):

        if len(nums) == len(curr):
            ans.append(curr.copy())
            return

        for index in count:
            if count[index] > 0:
                curr.append(index)
                count[index] -= 1
                self.permutations(nums, curr, ans, count)
                count[index] += 1
                curr.pop()

s = Solution()

print(s.permuteUnique([1,2,1,4]))
