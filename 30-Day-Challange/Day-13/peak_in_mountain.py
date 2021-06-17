class Solution:
    def peakIndexInMountainArray(self, arr):

        left = 0
        right = len(arr) - 1

        while left <= right:

            mid = left + (right - left)//2

            if mid == 0:
                lower = -sys.maxsize - 1
            else:
                lower = arr[mid - 1]

            if mid == len(arr) - 1:
                higher = -sys.maxsize - 1
            else:
                higher = arr[mid + 1]

            if lower < arr[mid] > higher:
                return mid

            if arr[mid] < higher:
                left = mid + 1
            else:
                right = mid - 1

s = Solution()
print(s.peakIndexInMountainArray([0, 2, 1, 0]))
