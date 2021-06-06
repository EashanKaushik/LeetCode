import sys

class Solution:
    def findLength(self, nums1, nums2):

        i = 0
        maximum = -sys.maxsize - 1

        while i < len(nums1):

            index = self.linear_search(nums2, nums1[i])

            print("Values: ", nums1[i], index)

            if index:
                index -= 1
                j = i
                while j + 1 < len(nums1) and index + 1 < len(nums2) and nums1[j + 1] == nums2[index + 1]:
                    print(j, i)
                    maximum = max(maximum, j - i + 2)

                    index += 1
                    j += 1

            i += 1

        return maximum

    def linear_search(self, nums, target):

        if target in nums:
            return nums.index(target) + 1
        else:
            return None

s = Solution()

print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
