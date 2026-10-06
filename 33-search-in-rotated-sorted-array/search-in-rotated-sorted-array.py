class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 1. Find the pivot index
        L, R = 0, len(nums)-1
        while L<=R:
            M = (L+R)//2

            if nums[M] == target:
                return M

            if nums[L] <= nums[M]:
                if nums[L] <= target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if nums[M] < target <= nums[R]:
                    L = M + 1
                else:
                    R = M - 1
        
        return -1
