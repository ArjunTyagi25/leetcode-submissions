class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = {}
        res = 0
        L = 0

        for R in range(len(nums)):
            if nums[R] in frequency:
                if frequency[nums[R]] == k:
                    while frequency[nums[R]] == k:
                        frequency[nums[L]] -= 1
                        L += 1
            frequency[nums[R]] = 1 + frequency.get(nums[R], 0)
            res = max(res, R-L+1)

        return res