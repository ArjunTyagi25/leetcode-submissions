class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_prefix = [nums[0]] * n
        min_suffix = [nums[-1]] * n

        for i in range(1, n):
            max_prefix[i] = max(max_prefix[i-1], nums[i])
        
        for i in range(n-2, -1, -1):
            min_suffix[i] = min(min_suffix[i+1], nums[i])

        for i in range(n):
            instability_score = max_prefix[i] - min_suffix[i]
            if instability_score <= k:
                return i

        return -1
        