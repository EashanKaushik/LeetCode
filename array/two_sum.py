def twoSum(self, nums, target):

    comp_set = dict()

    for index, num in enumerate(nums):
        comp = target - num
        if num not in comp_set.keys():
            comp_set[comp] = index
        else:
            return [comp_set[num], index]
