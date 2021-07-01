class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def get_index(self, char):

        if char.islower():
            return ord(char) - ord('a')
        else:
            return ord(char) - ord('A')

    def insert(self, word):

        curr_level = self.root

        for char in word:
            index = self.get_index(char)

            if not curr_level.children[index]:
                curr_level.children[index] = TrieNode()

            curr_level = curr_level.children[index]

        curr_level.word += 1

    def search(self, word):

        curr_level = self.root

        for char in word:

            index = self.get_index(char)

            if not curr_level.children[index]:
                return False

            curr_level = curr_level.children[index]

        if curr_level.word > 0:
            return True
        else:
            return False

    def startsWith(self, prefix):

        curr_level = self.root

        for char in prefix:

            index = self.get_index(char)

            if not curr_level.children[index]:
                return False

            curr_level = curr_level.children[index]

        return True
