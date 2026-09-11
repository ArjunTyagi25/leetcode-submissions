class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        window = set()
        L, res, curr_sum = 0, 0, 0

        for R in range(len(nums)):
            if len(window) < k:
                if nums[R] not in window:
                    window.add(nums[R])
                    curr_sum += nums[R]
                else:
                    while L <= R and nums[R] in window:
                        window.remove(nums[L])
                        curr_sum -= nums[L]
                        L += 1
                    window.add(nums[R])
                    curr_sum += nums[R]
            else:
                res = max(res, curr_sum)
                if nums[R] not in window:
                    window.add(nums[R])
                    curr_sum += nums[R]
                    window.remove(nums[L])
                    curr_sum -= nums[L]
                    L += 1
                else:
                    while L <= R and nums[R] in window:
                        window.remove(nums[L])
                        curr_sum -= nums[L]
                        L += 1
                    window.add(nums[R])
                    curr_sum += nums[R]

        if len(window) == k:
            res = max(res, curr_sum)

        return res


            

        