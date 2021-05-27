import sys
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        num = len(nums1) + len(nums2)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if num % 2 == 0:
            return(self.even(nums1, nums2, num))
        else:
            return(self.odd(nums1, nums2, num))

    def odd(self, num1, num2, num):
        i, j = self.partition(num1, num2, num)

        lefta, righta = self.get_partition(i, num1)
        leftb, rightb = self.get_partition(j, num2)

        b = min(righta, rightb)

        return b

    def even(self, num1, num2, num):

        i, j = self.partition(num1, num2, num)

        lefta, righta = self.get_partition(i, num1)
        leftb, rightb = self.get_partition(j, num2)

        a = max(lefta, leftb)
        b = min(righta, rightb)

        return (a + b) / 2

    def partition(self, num1, num2, num):
        n = num // 2
        i = j = k = 0

        while k < n and i < len(num1) and j < len(num2):
            if num1[i] >= num2[j]:
                j += 1
            elif num1[i] < num2[j]:
                i += 1
            k += 1

        while k < n and i < len(num1):
            k+= 1
            i+=1
        while k < n and j < len(num2):
            k+= 1
            j+=1

        return i, j

    def get_partition(self, i, num):

        left = right = None

        if i == 0:
            left = -sys.maxsize - 1
            if i == len(num):
                right = sys.maxsize
            else:
                right = num[i]
        elif i == len(num):
            left = num[i - 1]
            right = sys.maxsize
        else:
            left = num[i-1]
            right = num[i]

        return left, right


s = Solution()

print(s.findMedianSortedArrays([1], [2, 3, 4]))
