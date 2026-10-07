class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x
        while L<R:
            M = (L+R)//2

            if M*M > x:
                R = M
            else:
                L = M + 1

        if L == 0 or L == 1:
            return L
        return L-1

        