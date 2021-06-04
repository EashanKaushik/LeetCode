class Solution:
    def reversePairs(self, nums):
        count = 0

        count = self.merge_sort(nums)

        return count

    def merge_sort(self, nums):

        if len(nums) <= 1:
            return 0

        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        count = 0

        count += self.merge_sort(left)
        count += self.merge_sort(right)

        # count logic
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] <= 2 * right[j]:
                i += 1
                continue
            else:
                j += 1
                count += len(left) - i

        # merge logic
        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

        return count


s = Solution()

nums = [40, 25, 19, 12, 9, 6, 2]
print(s.reversePairs(nums))
