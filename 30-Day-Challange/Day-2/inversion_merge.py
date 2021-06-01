class Solution:
    def count_inverse(self, arr):

        return self.merge_sort(arr)

    def merge_sort(self, arr):
        count = 0

        if len(arr) > 1:

            # middle of length of array
            mid_index = len(arr) // 2

            # left and right arrays
            left = arr[:mid_index]
            right = arr[mid_index:]

            print(left)

            count += self.merge_sort(left)

            print (count)

            print(right)
            count += self.merge_sort(right)
            print(count)
            left_index = right_index = parent_index = 0


            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    arr[parent_index] = left[left_index]
                    left_index += 1
                else:
                    arr[parent_index] = right[right_index]
                    right_index += 1
                    count += 1
                parent_index += 1

            while left_index < len(left):
                arr[parent_index] = left[left_index]
                left_index += 1
                parent_index += 1

            while right_index < len(right):
                arr[parent_index] = right[right_index]
                right_index += 1
                parent_index += 1

            print('After', count)

        return count

s = Solution()

print(s.count_inverse([8, 4, 2, 1]))
