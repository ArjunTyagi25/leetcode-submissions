class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        min_k = float('inf')

        while L<R:
            k = (L+R)//2

            time = 0
            for p in piles:
                time += ceil(p/k)
                if time > h:
                    break

            if time > h:
                L = k + 1
            else:
                min_k = min(min_k, k)
                R = k

        return L
