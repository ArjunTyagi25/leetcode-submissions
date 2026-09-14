class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDist = 0
        for num in nums:
            if maxDist < 0:
                return False
            elif num > maxDist:
                maxDist = num
            maxDist -= 1
        return True

        