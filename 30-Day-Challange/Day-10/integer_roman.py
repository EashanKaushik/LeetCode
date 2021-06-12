class Solution:
    def intToRoman(self, num):
        symbol_value = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        roman = list()

        while num > 0:

            digits = len(str(num))

            zeros = 10 * digits

            remainder = num % zeros
            val = num - remainder

            if val / (zeros/10) == 9:

                greater = symbol_value[zeros]
                lesser = symbol_value[zeros/10]
                roman.extend([lesser, greater])

            elif val / (zeros/10) == 4:

                greater = symbol_value[zeros/2]
                lesser = symbol_valye[(zeros/2)/10]
                roman.extend([lesser, greater])
            else:

                for index, symbol in enumerate(symbol_value.keys()):
                    if remainder < symbol:
                        roman.append(lesser)
                        break

                    lesser = symbol_value[symbol] * remainder

            if val > 0:
                num = remainder
            else:
                num = 0

        return ''.join(roman)
