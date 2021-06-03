class Solution:
    def generate(self, numRows):

        output = [[1]]

        for row in range(2, numRows + 1):

            row_output = [0] * row
            prev = output[row - 2]

            row_output[0] = 1
            row_output[-1] = 1
            for col in range(1, len(row_output) - 1):
                row_output[col] = prev[col] + prev[col - 1]

            output.append(row_output)
        return output

s = Solution()

print(s.generate(5))
