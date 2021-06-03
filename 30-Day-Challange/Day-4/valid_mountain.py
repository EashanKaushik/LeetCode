class Solution:
    def validMountainArray(self, arr):

        if len(arr) < 3:
            return False

        i = 0
        inc, dec = False, False

        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            inc = True
            i += 1

        while i < len(arr) - 1 and arr[i] > arr[i + 1]:
            dec = True
            i += 1

        return inc and dec and i == len(arr) - 1


s = Solution()
print(s.validMountainArray([0,3,2,1]))
