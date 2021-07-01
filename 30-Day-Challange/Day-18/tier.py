class Tier:
    def __init__(self):
        self.children = [None] * 26
        self.complete_word = 0

    def __str__(self):
        return f'{self.children} and {self.complete_word}'

class WordDictionary:

    def __init__(self):
        self.root = Tier()
        self.found = list()

    def get_index(self, char):

        if char.isupper():
            return abs(ord('A') - ord(char))
        else:
            return abs(ord('a') - ord(char))

    def addWord(self, word):

        curr_level = self.root

        for char in word:
            index = self.get_index(char)

            if not curr_level.children[index]:
                curr_level.children[index] = Tier()
            curr_level = curr_level.children[index]

        curr_level.complete_word += 1


    def search(self, word):

        curr_level = self.root

        self.found = list()

        self.dfs(word, 0, curr_level)

        return True if self.found else False

    def dfs(self, word, index, curr_level):

        if index == len(word):
            if curr_level.complete_word > 0:
                self.found.append(True)
            return

        char = word[index]

        if char == '.':
            for level in curr_level.children:
                if level:
                    self.dfs(word, index + 1, level)
                    if self.found:
                        return
        else:
            i = self.get_index(char)

            if curr_level.children[i]:
                self.dfs(word, index + 1, curr_level.children[i])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

s = WordDictionary()
s.addWord('at')
s.addWord('and')
s.addWord('an')
s.addWord('at')
s.addWord('add')

print(s)
