from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Two frontiers instead of one queue
        front = {beginWord}
        back = {endWord}
        word_set.discard(beginWord)
        word_set.discard(endWord)

        length = 1
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        while front and back:
            # Always expand the smaller frontier for efficiency
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            for word in front:
                for i in range(len(word)):
                    original = word[i]
                    for c in alphabet:
                        if c == original:
                            continue
                        candidate = word[:i] + c + word[i+1:]
                        if candidate in back:
                            return length + 1
                        if candidate in word_set:
                            next_front.add(candidate)
                            word_set.discard(candidate)
            front = next_front
            length += 1

        return 0