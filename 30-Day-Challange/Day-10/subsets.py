class Solution:
    def subsets(self, nums):
        ans = list()
        curr= list()
        self.soln(ans,nums, curr ,0)

        return ans

    def soln(self, ans, nums, curr, index):
        if index >= len(nums):
            return

        ans.append(curr.copy())

        for i in range(index, len(nums)):
            if nums[i] not in curr:
                curr.append(nums[i])
                self.soln(ans, nums, curr, i)
                curr.pop()


s = Solution()
print(s.subsets([1, 2, 3]))
