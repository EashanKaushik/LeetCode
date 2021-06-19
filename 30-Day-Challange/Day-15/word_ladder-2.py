import sys
from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        queue = deque()
        words = set(wordList)
        level = 0
        word_found = False
        prospective_words = [chr(i) for i in range(ord('a'),ord('z')+1)]

        adj_matrix = defaultdict(set)
        if endWord not in words:
            return []

        if beginWord in words:
            words.remove(beginWord)

        queue.append((beginWord, 1))

        while len(queue) > 0:

            curr_word, level = queue.popleft()

            if curr_word == endWord and not word_found:
                word_found = True
                word_at = level

            for index in range(0, len(curr_word)):
                for w in prospective_words:

                    if w == curr_word[index]:
                        continue

                    new_word = curr_word[:index] + w + curr_word[index + 1:]

                    if new_word in words:
                        adj_matrix[curr_word].add(new_word)
                        queue.append((new_word, level + 1))
                        if new_word != endWord:
                            words.remove(new_word)
                    elif new_word in wordList:
                        adj_matrix[curr_word].add(new_word)

        if not word_found:
            return []
        else:
            print(words)
            output = list()
            current = [beginWord]
            print(adj_matrix)
            self.dfs(set(wordList), endWord, current, output, word_at-1, prospective_words, adj_matrix)

            return output

    def dfs(self, words, endWord, current, output, level, prospective_words, adj_matrix):

        if level == 0 and current[-1] == endWord:
            output.append(current.copy())
            return
        elif level == 0:
            return

        curr_word = current[-1]

        for index in range(0, len(curr_word)):

            for new_word in adj_matrix[curr_word]:

                if new_word in words:

                    words.remove(new_word)
                    current.append(new_word)
                    self.dfs(words.copy(), endWord, current, output, level-1, prospective_words, adj_matrix)
                    current.pop()

s = Solution()

print(s.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
