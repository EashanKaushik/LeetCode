class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        chars = dict()

        index = 0

        while index < len(s):

            if s[index] in chars:
                chars[s[index]] += 1
            else:
                chars[s[index]] = 1

            if t[index] in chars:
                chars[t[index]] -= 1
            else:
                chars[t[index]] = -1

            index += 1

        for _, value in chars.items():
            if value == 0:
                continue

            return False


        return True


s = Solution()

print(s.isAnagram("anagram", "nagaram"))
