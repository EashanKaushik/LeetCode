class Solution:
    def nextPermutation(self, nums):

        index = len(nums) - 2
        found = False

        while index >= 0:
            if nums[index] < nums[index + 1]:
                found = True
                break

            index -= 1

        index_two = len(nums) - 1

        while index_two >= 0 and found:
            if nums[index_two] > nums[index]:
                nums[index], nums[index_two] = nums[index_two], nums[index]
                nums[index + 1:] = nums[-1: index:-1]
                break
            index_two -= 1

        if not found:
            nums.sort()




s = Solution()

# arr = [2, 3, 1]
# arr = [1, 3, 5, 4, 2]
# arr = [3, 2, 1]
# arr = [1]
# arr = [1, 2]
# arr = [2, 1]
arr = [3, 1, 2]

s.nextPermutation(arr)

print(arr)
