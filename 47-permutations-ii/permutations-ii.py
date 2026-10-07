class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)

        def rec(currPerm):
            if len(currPerm) == len(nums):
                res.append(currPerm.copy())

            i = 0
            while i < len(nums):
                if used[i]:
                    i += 1
                    continue
                
                used[i] = True
                currPerm.append(nums[i])
                rec(currPerm)
                currPerm.pop()
                used[i] = False
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1
                
                i += 1

        rec([])
        return res
        