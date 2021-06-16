class Solution:
    def search(self, nums, target):

        index = 0
        while index + 1 < len(nums) and nums[index] <= nums[index + 1]:
            index += 1

        left = 0
        right = len(nums) - 1

        if index == len(nums) - 1:
            return self.binary_search(nums, left, right, target)
        else:
            if nums[0] <= target <= nums[index]:
                return self.binary_search(nums, left, index, target)
            elif nums[index + 1] <= target <= nums[right]:
                return self.binary_search(nums, index + 1, right, target)

    def binary_search(self, nums, left, right, target):

        while left <= right:

            mid = left + (right - left)//2

            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


s = Solution()
print(s.search([2,5,6,0,0,1,2], 0))
