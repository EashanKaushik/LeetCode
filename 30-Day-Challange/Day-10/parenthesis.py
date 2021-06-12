class Solution:
    def isValid(self, s):

        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = list()

        not_valid = True

        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    not_valid = False
                    break

                recent_open = stack.pop()

                if bracket != brackets[recent_open]:
                    not_valid = False
                    break

        if len(stack) > 0:
            not_valid = False

        return not_valid if not_valid else not_valid


s = Solution()

print(s.isValid("{[{]}"))
