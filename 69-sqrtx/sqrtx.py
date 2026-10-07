class Solution:
    def mySqrt(self, x: int) -> int:
        L, R = 0, x+1
        while L<R:
            M = (L+R)//2

            if M*M > x:
                R = M
            else:
                L = M + 1

        return L-1

        