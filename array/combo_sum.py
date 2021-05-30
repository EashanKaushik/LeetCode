class Solution:
    def combinationSum(self, candidates, target):

        combo = list()

        for i, num in enumerate(candidates):

            start = num
            all_sum = set()

            if target % num == 0:
                combo.append([num] * (target // num))

            while start < target:
                all_sum.add(target - start)
                start += num

            for index in range(i + 1, len(candidates)):
                if candidates[index] in all_sum:
                    complement = target - candidates[index]
                    combo.append([candidates[index]] + [num] * (complement // num))

        return combo

s = Solution()

print(s.combinationSum([2,3,5], 8))
