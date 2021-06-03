# dutch national flag solution
# OR
# Count sort
class Solution:
    def sortColors(self, nums):
        zero = 0
        two = len(nums) - 1

        start = 0

        while (start <= two):

            # print(start, zero, two)

            if nums[start] == 0:
                nums[zero], nums[start] = nums[start], nums[zero]
                zero += 1
            elif nums[start] == 2:
                nums[two], nums[start] = nums[start], nums[two]
                two -= 1
                continue


            start += 1

s = Solution()

# arr = [2, 0, 1]
# arr =[2, 0, 2, 1, 1, 0]
arr = [1]

s.sortColors(arr)

print(arr)
