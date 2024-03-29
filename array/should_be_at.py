class Solution:
    def searchInsert(self, nums, target):

        if not nums:
            return 0

        left = 0
        right = len(nums) - 1

        while(left <= right):

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left
        return left

s = Solution()

print(s.searchInsert([1,3,5,6], 0))
