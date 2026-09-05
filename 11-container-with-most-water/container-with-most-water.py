class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = float('-inf')
        L, R = 0, len(height)-1

        while L<R:
            h1 = height[L]
            h2 = height[R]
            
            if h1 < h2:
                area = h1 * (R-L)
                L += 1
            else:
                area = h2 * (R-L)
                R -= 1

            if area > res:
                res = area
            
        return res
            
        