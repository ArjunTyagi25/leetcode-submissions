class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_c = int(sqrt(c))

        for i in range(sqrt_c+1):
            target = c - i*i
            root = int(sqrt(target))
            
            if root * root == target:
                return True

        return False 
        