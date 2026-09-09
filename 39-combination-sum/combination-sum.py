class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def rec(i, cur_combination, cur_sum):
            if cur_sum == target:
                self.res.append(cur_combination.copy())

            if cur_sum > target or i == len(candidates):
                return


            for j in range(i, len(candidates)):
                cur_combination.append(candidates[j])
                rec(j, cur_combination, cur_sum + candidates[j])
                cur_combination.pop()

            return

        rec(0, [], 0)
        return self.res