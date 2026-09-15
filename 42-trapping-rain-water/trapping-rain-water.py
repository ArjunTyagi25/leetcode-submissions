class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = height[stack.pop()]
                if stack:
                    min_height = min(height[stack[-1]], height[i])
                    width = i - stack[-1] - 1
                    res += (min_height - bottom) * width
            stack.append(i)

        return res

'''
     i    0,1,2,3,4,5,6,7,8,9,10,11
height = [0,1,0,2,1,0,1,3,2,1,2,1]
stack  = [1,2]
bottom = 
res
'''