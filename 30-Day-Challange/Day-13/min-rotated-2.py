class Solution:
    def findMin(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2

            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                continue

            if nums[mid] >= nums[left] and nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left] and nums[mid] <= nums[right]:
                right = mid - 1
            else:
                break

        return nums[left]



s = Solution()

print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
