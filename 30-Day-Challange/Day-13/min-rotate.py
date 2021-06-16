class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:

            mid = left + (right - left)//2
            print(mid, left, right)

            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                left = mid + 1
                print('F', left)
            elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                left = mid
                print('S', left)
            elif nums[left] > nums[mid] and nums[mid] > nums[right]:
                left = mid + 1
                print('T', left)
            else:
                right = mid - 1
                print('Forth', right)

        return nums[left]

s = Solution()

print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
