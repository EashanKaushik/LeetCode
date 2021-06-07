class Solution:
    def maxScore(self, arr, k):

        dp = {'l':[0], 'r':[0]}

        curr_sum_left = 0
        curr_sum_right = 0

        for index in range(0, k):

            # for left
            curr_sum_left += arr[index]
            dp['l'].append(curr_sum_left)

            # for right
            j = len(arr) - 1 - index
            curr_sum_right += arr[j]
            dp['r'].append(curr_sum_right)

        maximum = -1
        left = 0
        right = k

        while k >= 0:
            curr_sum = dp['l'][left] + dp['r'][right]

            left += 1
            right -= 1

            maximum = max(curr_sum, maximum)

            k -= 1

        return maximum


s = Solution()
print(s.maxScore([30,88,33,37,18,77,54,73,31,88,93,25,18,31,71,8,97,20,98,16,65,40,18,25,13,51,59], 26))
