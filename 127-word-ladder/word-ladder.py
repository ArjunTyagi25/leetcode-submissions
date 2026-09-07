class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = set(wordList)
        if endWord not in dictionary:
            return 0

        q = deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        distance = 1

        while q:
            for i in range(len(q)):
                current_word = q.popleft()

                if current_word == endWord:
                    return distance
                
                for i in range(len(current_word)):
                    for j in range(97, 123, 1):
                        next_word = current_word[:i] + chr(j) + current_word[i+1:]

                        if next_word in dictionary and next_word not in visited:
                            q.append(next_word)
                            visited.add(next_word)

            if not q:
                return 0
            else:
                distance += 1
        