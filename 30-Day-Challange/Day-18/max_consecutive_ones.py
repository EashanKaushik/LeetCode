class Solution:
    def longestOnes(self, nums, k):

        if not nums:
            return 0

        del_pointer = insert_pointer = 0
        count_one = 0
        current_added = 0
        current_max = 0

        while insert_pointer < len(nums):

            if nums[insert_pointer] == 0:

                if current_added < k:
                    current_added += 1
                    insert_pointer += 1


                    if insert_pointer - del_pointer > current_max:
                        current_max = insert_pointer - del_pointer

                else:

                    while nums[del_pointer] != 0:
                        del_pointer += 1

                    del_pointer += 1
                    current_added -= 1

            elif nums[insert_pointer] == 1:


                insert_pointer += 1

                if insert_pointer - del_pointer > current_max:
                        current_max = insert_pointer - del_pointer

        return current_max
