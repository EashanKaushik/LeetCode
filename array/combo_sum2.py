class Solution:
    def combinationSum2(self, candidates, target):

        combo_list = list()
        result = list()

        self.combo_sum(0, candidates, target, combo_list, result)

        return result

    def combo_sum(self, start, candidates, target, combo_list, result):

        if target == 0:
            result.append(combo_list)

        if target < 0:
            return

        for index in range(start, len(candidates)):
            self.combo_sum(index + 1, candidates, target - candidates[index], [candidates[index]] + combo_list, result)


s = Solution()

print(s.combinationSum2([10,1,2,7,6,1,5], 8))
