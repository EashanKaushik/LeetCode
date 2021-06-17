import math
import sys
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            nums1, nums2 = nums2, nums1

        if (n1 + n2) % 2 == 0:
            return self.even(nums1, nums2)
        else:
            return self.odd(nums1, nums2)

    def even(self, nums1, nums2):

        left1, left2, right1, right2 = self.partition(nums1, nums2)


        return (max(left1, left2) + min(right1, right2)) / 2

    def odd(self, nums1, nums2):

        left1, left2, right1, right2 = self.partition(nums1, nums2)

        return max(left1, left2)

    def partition(self, nums1, nums2):

        left = 0
        right = len(nums1)
        elements_in_left = (len(nums1) + len(nums2) + 1) // 2

        while left <= right:

            partition1 = left + (right-left) // 2
            partition2 = elements_in_left - partition1

            left1 = -sys.maxsize - 1 if partition1 == 0 else nums1[partition1-1]
            right1 = sys.maxsize if partition1 == len(nums1) else nums1[partition1]

            left2 = -sys.maxsize - 1 if partition2 == 0 else nums2[partition2-1]
            right2 = sys.maxsize if partition2 == len(nums2) else nums2[partition2]

            if left1 <= right2 and left2 <= right1:
                return left1, left2, right1, right2
            elif left2 > right1:
                left = partition1 + 1
            else:
                right = partition1 - 1


s = Solution()

print(s.findMedianSortedArrays([1, 2], [2]))
