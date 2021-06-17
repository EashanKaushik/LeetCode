class Solution:
    def findPeakElement(self, nums):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left)//2

            if mid == 0:
                lower = -sys.maxsize - 1
            else:
                lower = nums[mid-1]

            if mid == len(nums) - 1:
                higher = -sys.maxsize - 1
            else:
                higher = nums[mid + 1]

            if lower < nums[mid] > higher:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


s = Solution()
print(s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
