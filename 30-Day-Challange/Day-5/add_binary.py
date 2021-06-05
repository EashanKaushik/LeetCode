class Solution:
    def addBinary(self, a: str, b: str) -> str:

        bit_a = len(a) - 1
        bit_b = len(b) - 1
        remainder = 0
        output = str()

        while bit_a >= 0 and bit_b >= 0:
            value = int(a[bit_a]) + int(b[bit_b]) + remainder

            if value == 2:
                remainder = 1
                value = 0
            elif value == 3:
                remainder = 1
                value = 1
            else:
                remainder = 0

            output += str(value)
            bit_a -= 1
            bit_b -= 1

        while bit_a >= 0:
            value = int(a[bit_a]) + remainder
            if value == 2:
                remainder = 1
                value = 0
            elif value == 3:
                remainder = 1
                value = 1
            else:
                remainder = 0
            output += str(value)
            bit_a -= 1

        while bit_b >= 0:
            value = int(b[bit_b]) + remainder
            if value == 2:
                remainder = 1
                value = 0
            elif value == 3:
                remainder = 1
                value = 1
            else:
                remainder = 0
            output += str(value)
            bit_b -= 1

        if remainder != 0:
            output += str(remainder)

        return output[::-1]
        
