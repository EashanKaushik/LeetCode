import sys

class Solution:
    def minWindow(self, s, t):

        count_map = dict()
        total_sum = 0
        for char in t:
            if char in count_map:
                count_map[char] += 1
                total_sum += 1
            else:
                count_map[char] = 1
                total_sum += 1


        found_on = list()
        minimum = sys.maxsize
        found = False
        start = None
        end = None
        left = 0
        right = 0

        while right < len(s):
            char = s[right]

            if char in count_map:
                count_map[char] -= 1
                total_sum -= 1
                found_on.append(right)

            while total_sum <= 0 and all(x <= 0 for x in count_map.values()) and left <= right:
                left = found_on[0]
                found = True
                if (minimum > len(s[found_on[0]: found_on[-1] + 1])):
                    minimum = len(s[found_on[0]: found_on[-1] + 1])
                    start, end = found_on[0], found_on[-1]
                remove = found_on.pop(0)
                count_map[s[remove]] += 1
                total_sum += 1

            right += 1

        if found:
            return s[start:end + 1]
        else:
            return ""


s = Solution()

# print(s.minWindow("ADOBECODEBANC", "ABC"))

print(s.minWindow("bba", "ab"))
