class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''
        Two conditions:
        1. If top of stack > heights[i], then increment res for top of stack and push current index to stack
        2. If top of stack < heights[i], then until top of stack becomes larger again, increment res for top of stack and pop it. Ultimately push the current index to the stack
        '''
        
        stack = []
        res = [0] * len(heights)

        for i in range(len(heights)):
            if stack != []:
                if stack[-1][0] > heights[i]:
                    res[stack[-1][1]] += 1
                else:
                    while stack and stack[-1][0] < heights[i]:
                        res[stack[-1][1]] += 1
                        stack.pop()

                    if stack:
                        res[stack[-1][1]] += 1
            stack.append([heights[i], i])
        
        return res



        return res

        