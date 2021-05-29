class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1
        found = None

        while left < right:


            mid = (left + right) // 2
            # print(left, right, mid)

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid


        if left != 0:
            found = self.binary_search(left, len(nums) - 1, nums, target)
            if not found:
                found = self.binary_search(0, left - 1, nums, target)
        else:
            found = self.binary_search(0, len(nums) - 1, nums, target)

        return found if found is not None else -1

    def binary_search(self, start, end, nums, target):

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        if nums[start] == target:
            return start

s = Solution()

print(s.search([4,5,6,7,0,1,2], 0))
