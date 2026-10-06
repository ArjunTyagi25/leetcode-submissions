class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        def rec(i, currComb, currTotal):
            if currTotal == target:
                res.append(currComb.copy())
                return
            
            if i == len(candidates) or currTotal > target:
                return

            currComb.append(candidates[i])
            rec(i+1, currComb, currTotal + candidates[i])
            currComb.pop()

            while i != len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            rec(i+1, currComb, currTotal)

        rec(0, [], 0)
        return res
            