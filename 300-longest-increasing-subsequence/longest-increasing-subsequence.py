class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def rec(curr_index):
            if memo[curr_index] != -1:
                return memo[curr_index]

            res = 1
            for j in range(curr_index+1, len(nums)):
                if nums[curr_index] < nums[j]:
                    res = max(res, 1 + rec(j))
            
            memo[curr_index] = res
            return res

        return max(rec(i) for i in range(len(nums)))
        