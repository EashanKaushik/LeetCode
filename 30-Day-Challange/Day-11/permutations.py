class Solution:
    def permute(self, nums):

        ans = list()
        curr = list()
        self.permutations(nums, curr, ans)

        return ans

    def permutations(self, nums, curr, ans):

        if len(nums) == 0:
            ans.append(curr.copy())
            return

        for index in range(0, len(nums)):
            temp = nums.pop(index)
            curr.append(temp)
            self.permutations(nums, curr, ans)
            curr.pop()
            nums.insert(index, temp)

s = Solution()

print(s.permutations([1,2,3,4]))
