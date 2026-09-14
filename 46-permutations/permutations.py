class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        visited = set()

        def rec(curr_perm):
            if len(curr_perm) == len(nums):
                self.res.append(curr_perm[:])
                return

            for num in nums:
                if num not in visited:
                    curr_perm.append(num)
                    visited.add(num)
                    rec(curr_perm)
                    curr_perm.pop()
                    visited.remove(num)

        rec([])
        return self.res