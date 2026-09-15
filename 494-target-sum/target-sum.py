class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.res = 0
        memo = {}
        def rec(i, curr_total):
            if i == len(nums):
                if curr_total == target:
                    return 1
                else:
                    return 0

            if (i, curr_total) in memo:
                return memo[(i, curr_total)]

            # Add the current number to curr_total
            res = rec(i+1, curr_total + nums[i])

            # Subtract the current number from curr_total
            res += rec(i+1, curr_total - nums[i])
            memo[(i, curr_total)] = res

            return res

        
        return rec(0, 0)

        