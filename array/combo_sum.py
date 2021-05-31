class Solution:
    def combinationSum(self, candidates, target):

        result = list()
        combo_list = list()

        self.back_track(0, candidates, target, combo_list, result)

        return result

    def back_track(self, start, nums, target, combo_list, result):

        if target < 0:
            return

        if target == 0:
            result.append(combo_list.copy())
            return

        for index in range(start, len(nums)):
            print('Inside', index, nums, target - nums[index], combo_list + [nums[index]], result)
            self.back_track(index, nums, target - nums[index], combo_list + [nums[index]], result)
            print('Outside', combo_list, result)

s = Solution()

print(s.combinationSum([2, 3, 5], 8))
