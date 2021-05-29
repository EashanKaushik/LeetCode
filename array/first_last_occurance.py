class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        return [self.left_most(nums, target), self.right_most(nums, target)]

    def left_most(self, nums, target):

        left = 0
        right = len(nums) - 1
        found = -1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                found = mid
                right = mid -1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return found


    def right_most(self, nums, target):

        left = 0
        right = len(nums) - 1
        found = -1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                found = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return found

s = Solution()

print(s.searchRange([5, 7, 7, 8, 8, 9, 10], 7))
