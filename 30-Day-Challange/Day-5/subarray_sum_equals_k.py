class Solution:
    def subarraySum(self, nums, k):

        sum_map = dict()
        sum_map[0] = 1
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num

            if curr_sum - k in sum_map:
                count += sum_map[curr_sum - k]

            if curr_sum in sum_map:
                sum_map[curr_sum] += 1
            else:
                sum_map[curr_sum] = 1

        return count
