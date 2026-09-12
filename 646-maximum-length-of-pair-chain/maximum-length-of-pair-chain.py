class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        curr_end_time = float('-inf')

        for i in range(len(pairs)):
            if curr_end_time < pairs[i][0]:
                count += 1
                curr_end_time = pairs[i][1]

        return count
        