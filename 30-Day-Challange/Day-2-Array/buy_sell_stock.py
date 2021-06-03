import sys

class Solution:
    def maxProfit(self, prices):

        minimum = sys.maxsize
        profit = 0
        for price in prices:

            if price < minimum:
                minimum = price

            if profit < price - minimum:
                profit = price - minimum

        return profit

s = Solution()

print(s.maxProfit([7, 1, 5, 3, 6, 4]))
