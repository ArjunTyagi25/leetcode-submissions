class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        memo = {}
        def rec(L, R, turn):
            if L > R:
                return 0

            state = (L, R, turn)
            if state in memo:
                return memo[state]

            if turn == "add":
                res_1 = nums[L] + rec(L+1, R, "sub")
                res_2 = nums[R] + rec(L, R-1, "sub")

                res = max(res_1, res_2)
            else:
                res_1 = -nums[L] + rec(L+1, R, "add")
                res_2 = -nums[R] + rec(L, R-1, "add")

                res = min(res_1, res_2)

            memo[state] = res
            return res

        return rec(0, len(nums)-1, "add") >= 0