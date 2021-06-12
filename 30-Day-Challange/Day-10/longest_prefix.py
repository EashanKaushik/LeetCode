class Solution:
    def longestCommonPrefix(self, strs):

        common_word = list()
        index = 0
        word_index = 0
        found = True
        temp = str()
        check = str()

        while 1:

            if index >= len(strs):
                index = 0
                word_index += 1
                common_word.append(check)

            if word_index >= len(strs[index]):
                return ''.join(common_word)

            if index == 0:
                check = strs[0][word_index]
            else:
                temp = strs[index][word_index]
                if temp != check:
                    return ''.join(common_word)

            index += 1


s = Solution()

print(s.longestCommonPrefix(['flower', 'flow', 'flight']))
