class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        L, R = 0, len(nums)
        start, end = -1, -1
        while L<R:
            M = (L+R)//2

            if nums[M] > target:
                R = M
            elif nums[M] < target:
                L = M + 1
            else:
                start = M
                R = M
        
        if start == -1:
            return [-1, -1]
        L, R = start, len(nums)
        while L<R:
            M = (L+R)//2

            if nums[M] > target:
                R = M
            elif nums[M] < target:
                L = M + 1
            else:
                end = M
                L = M + 1

        return [start, end]
    