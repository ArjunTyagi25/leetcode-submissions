class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float('inf')
        runningSum = 0
        L = 0
        for R in range(len(nums)):
            runningSum += nums[R]

            while L<=R and runningSum >= target:
                res = min(res, R-L+1)
                runningSum -= nums[L]
                L += 1

        if res == float('inf'):
            return 0
        return res