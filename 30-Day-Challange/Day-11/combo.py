class Solution:
    def combine(self, n, k):

        ans = list()
        curr = list()

        # nums = [number for number in range(1, n + 1)]

        self.generate(1, n, curr, ans, k)

        return ans

    def generate(self, start, end, curr, ans, limit):

        if len(curr) == limit:
            ans.append(curr.copy())
            return

        # temp = nums.copy()
        for index in range(start, end + 1):
            curr.append(index)
            self.generate(index + 1, end,curr, ans, limit)
            curr.pop()

        

s = Solution()

print(s.combine(4, 2))
