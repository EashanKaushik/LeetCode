class Solution:
    def findMaxLength(self, nums):

        curr_sum_dict = {0:-1}
        curr_sum = 0

        maximum = -1
        index = 0

        while index < len(nums):
            num = nums[index]

            if num == 0:
                curr_sum -= 1
            else:
                curr_sum += 1


            if curr_sum not in curr_sum_dict:
                curr_sum_dict[curr_sum] = index
            else:
                maximum = max(maximum, index - curr_sum_dict[curr_sum])

            index += 1

        return maximum if maximum != -1 else 0


s = Solution()

print(s.findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]))
