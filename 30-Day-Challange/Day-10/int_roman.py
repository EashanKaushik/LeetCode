import math
class Solution:
    def intToRoman(self, num):
        symbol_value = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',

        }

        roman = str()

        while num > 0:

            digits = len(str(num))

            zeros = int(math.pow(10, digits))

            remainder = num % int(zeros/ 10)
            val = num - remainder

            if val / (zeros/10) == 9:

                roman += symbol_value[zeros/10]
                roman += symbol_value[zeros]

                if val > 0:
                    num = remainder
                else:
                    num = 0

            elif val / (zeros/10) == 4:

                roman += symbol_value[zeros/10]
                roman += symbol_value[zeros/2]

                if val > 0:
                    num = remainder
                else:
                    num = 0
            else:

                x = self.binary_search(val)
                roman += symbol_value[x]
                num -= x

        return roman

    def binary_search(self, val):
        found = False
        nums = [1, 5, 10, 50, 100, 500, 1000]

        left = 0
        right = 6

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] > val:
                right = mid - 1
            elif nums[mid] < val:
                left = mid + 1
            else:
                found = True
                break

        if found:
            return nums[mid]

        return nums[right]


s = Solution()

print(s.intToRoman(2949))
