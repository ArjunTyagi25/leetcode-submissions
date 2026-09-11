class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = set()
        L = 0
        curr_sum = 0
        res = float('-inf')

        for R in range(len(nums)):
            while nums[R] in window:
                curr_sum -= nums[L]
                window.remove(nums[L])
                L += 1
            
            window.add(nums[R])
            curr_sum += nums[R]
            res = max(res, curr_sum)

        return res