class Solution:
    def merge(self, intervals):

        intervals.sort()

        i = 0

        # result = list()

        while i < len(intervals) - 1:

            curr = intervals[i]
            next_ = intervals[i + 1]

            if max(curr) >= min(next_):
                intervals.pop(i)
                intervals.pop(i)
                if max(curr) > max(next_):
                    intervals.insert(i, curr)
                else:
                    intervals.insert(i, [min(curr), max(next_)])
                continue

            i += 1

        return intervals


s = Solution()

print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
