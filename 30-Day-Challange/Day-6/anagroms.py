class Solution:
    def groupAnagrams(self, strs):

        index = dict()
        count = 0
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in index:
                index[sorted_word] = [word]
            else:
                index[sorted_word].append(word)

        return index.values()


s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
