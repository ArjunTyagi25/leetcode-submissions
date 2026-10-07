class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        L, R = 0, len(nums)
        while L<R:
            M = (L+R)//2

            if nums[M] >= target:
                R = M
            else:
                L = M + 1

        return L