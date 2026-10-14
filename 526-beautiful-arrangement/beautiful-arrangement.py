class Solution:
    def countArrangement(self, n: int) -> int:
        
        def rec(currIndex, usedNums):
            if currIndex == n+1:
                return 1

            res = 0
            for i in range(1, n+1):
                if (currIndex % i == 0 or i % currIndex == 0) and i not in usedNums:
                    usedNums.add(i)
                    res += rec(currIndex+1, usedNums)
                    usedNums.remove(i)

            return res

        return rec(1, set())