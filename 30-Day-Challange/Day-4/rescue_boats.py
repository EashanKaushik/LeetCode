class Solution:
    def numRescueBoats(self, people, limit):

        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            current_weight = people[left] + people[right]

            if current_weight <= limit:
                left += 1
                right -= 1
            else:
                right -= 1

            boats += 1
        return boats
        

s = Solution()

print(s.numRescueBoats([5, 1, 4, 2], 6))
