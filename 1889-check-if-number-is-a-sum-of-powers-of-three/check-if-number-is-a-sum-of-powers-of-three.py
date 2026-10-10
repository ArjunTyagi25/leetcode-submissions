class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        possiblePowers = [i for i in range(17)]
        memo = {}
        def rec(i, currTotal):
            if currTotal == n:
                return True

            if currTotal > n or i == len(possiblePowers):
                return False

            if (i, currTotal) in memo:
                return memo[(i, currTotal)]

            res = rec(i+1, currTotal + pow(3, i)) or rec(i+1, currTotal)
            memo[(i, currTotal)] = res
            
            return res

        return rec(0, 0)