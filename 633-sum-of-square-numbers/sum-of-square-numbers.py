class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_c = int(sqrt(c))

        start, end = 0, sqrt_c

        while start <= end:
            curr_c = start * start + end * end

            if curr_c < c:
                start += 1
            elif curr_c > c:
                end -= 1
            else:
                return True

        return False
        