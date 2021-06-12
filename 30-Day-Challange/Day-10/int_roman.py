import math
import sys
class Solution:
    def intToRoman(self, num):
        # symbol_value = {
        #     1: 'I',
        #     5: 'V',
        #     10: 'X',
        #     50: 'L',
        #     100: 'C',
        #     500: 'D',
        #     1000: 'M',
        #     sys.maxsize: ''
        # }
        roman = list()

        while num > 0:

            digits = len(str(num))

            zeros = int(math.pow(10, digits))

            remainder = num % int(zeros/ 10)
            val = num - remainder

            print(remainder, val)

            if val / (zeros/10) == 9:
                print('Inside 9')

                greater = symbol_value[zeros]
                lesser = symbol_value[zeros/10]
                roman.extend([lesser, greater])
                if val > 0:
                    num = remainder
                else:
                    num = 0

            elif val / (zeros/10) == 4:
                print('Inside 4')

                greater = symbol_value[zeros/2]
                lesser = symbol_value[zeros/10]
                roman.extend([lesser, greater])
                if val > 0:
                    num = remainder
                else:
                    num = 0
            else:
                print('Inside other')
                if val in symbol_value:
                    roman.append(symbol_value[val])
                    num -= val
                else:
                    for index, symbol in enumerate(symbol_value.keys()):

                        if val < symbol:
                            roman.append(lesser)
                            num = temp
                            break

                        lesser = symbol_value[symbol]
                        temp = num - symbol

        return ''.join(roman)


s = Solution()
print(s.intToRoman(2000))
