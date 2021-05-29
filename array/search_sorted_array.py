class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1
        pivot = 0

        if left == right:
            if nums[left] == target:
                return 0

        mid = (left + right) // 2

        while mid != left:

            if nums[left] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid
            else:
                pivot = mid
                print(pivot)
                if nums[0] <= target <= nums[pivot]:
                    found = self.binary_search(0, pivot, nums, target)
                elif nums[pivot + 1] <= target <= nums[len(nums) - 1]:
                    print('f')
                    found = self.binary_search(pivot + 1, len(nums) - 1, nums, target)
                break

            mid = (left + right) // 2

        found = None



        return found if found else -1

    def binary_search(self, start, end, arr, target):

        mid = (start + end) // 2

        while mid != start:

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid
            else:
                start = mid

            mid = (start + end) // 2

        if arr[start] == target:
            return start

        if arr[end] == target:
            return end

s = Solution()

print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
