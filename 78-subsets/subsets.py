class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def rec(i, curr_subset):
            if i == len(nums):
                self.res.append(curr_subset.copy())
                return

            # Don't pick the number at i
            rec(i+1, curr_subset)

            # Pick the number at i
            curr_subset.append(nums[i])
            rec(i+1, curr_subset)
            curr_subset.pop()

        rec(0, [])
        return self.res