class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        def rec(i):
            if pow(3, i) == n:
                return True
            elif pow(3, i) > n:
                return False
            else:
                return rec(i+1)

        return rec(0)
        