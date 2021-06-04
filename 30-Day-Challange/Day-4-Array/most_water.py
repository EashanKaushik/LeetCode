import sys
class Solution:
    def maxArea(self, height):

        i = 0
        j = len(height) - 1

        x = j
        h = min(height[i], height[j])
        max_area = -sys.maxsize - 1
        area = 0
        while x > 0:

            area = x * h

            if area > max_area:
                max_area = area

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

            h = min(height[i], height[j])

            x -= 1

        return max_area


s = Solution()

print(s.maxArea([4,3,2,1,4]))
