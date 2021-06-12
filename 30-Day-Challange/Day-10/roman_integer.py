class Solution:
    def romanToInt(self, s):
        symbol_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        index = 0
        count = 0
        while index < len(s):
            symbol = s[index]

            if index + 1 < len(s):
                if symbol_value[symbol] < symbol_value[s[index + 1]]:
                    count += symbol_value[s[index + 1]] - symbol_value[symbol]
                    index += 2
                else:
                    count += symbol_value[symbol]
                    index += 1
            else:
                count += symbol_value[symbol]
                index += 1

        return count


s = Solution()
print(s.romanToInt("XLIX"))
