
def binary_search(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = left + (right - left)//2

        if nums[mid] == target:
            return True

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False

print(binary_search([2,4,6,8,9,10,12,56,63], 56))
