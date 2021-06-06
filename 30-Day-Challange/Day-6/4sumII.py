class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):

        n = len(nums1)
        sum_map = dict()

        for i in range(0, n):

            for j in range(0, n):

                curr_sum = nums1[i] + nums2[j]

                if curr_sum in sum_map:
                    sum_map[curr_sum] += 1
                else:
                    sum_map[curr_sum] = 1

        count = 0

        for k in range(0, n):

            for l in range(0, n):

                curr_sum = nums3[k] + nums4[l]

                if -curr_sum in sum_map:
                    count += sum_map[-curr_sum]

        return count
