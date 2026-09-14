class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target = target/2
        memo = {}
        def rec(remaining_amount, i):
            if remaining_amount == 0:
                return True
            
            if remaining_amount < 0 or i == len(nums):
                return False

            if (remaining_amount, i) in memo:
                return memo[(remaining_amount, i)]

            res = rec(remaining_amount - nums[i], i+1) or rec(remaining_amount, i+1)
            memo[(remaining_amount, i)] = res
            return res

        return rec(target, 0)

        