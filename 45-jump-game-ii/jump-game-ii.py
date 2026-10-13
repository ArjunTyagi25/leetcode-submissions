class Solution:
    def jump(self, nums: list[int]) -> int:
        memo = {}
        def rec(currIndex):
            if currIndex == len(nums) - 1:
                return 0

            if currIndex >= len(nums):
                return float('inf')

            if currIndex in memo:
                return memo[currIndex]

            res = float('inf')
            for i in range(nums[currIndex], 0, -1):
                nextIndex = currIndex + i
                res = min(res, 1 + rec(nextIndex))

            memo[currIndex] = res
            return res

        return rec(0)