class Solution:
    def removeElement(self, nums, val):

        count = 0

        index = times = 0

        while times < len(nums):

            if nums[index] == val:
                nums.pop(index)
                nums.append(val)
            else:
                count += 1
                index += 1

            times += 1

        return count

arr = [3, 2, 2, 3]

s = Solution()

print(s.removeElement(arr, 3))

print(arr)
