class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        possiblePowers = [i for i in range(17)]

        def rec(i, currTotal):
            if currTotal == n:
                return True

            if currTotal > n or i == len(possiblePowers):
                return False

            res = rec(i+1, currTotal + pow(3, i)) or rec(i+1, currTotal)
            return res

        return rec(0, 0)