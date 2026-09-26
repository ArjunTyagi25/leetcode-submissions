class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            if curr_sum >= 0:
                curr_sum += num
            else:
                curr_sum = num

            if curr_sum > max_sum:
                max_sum = curr_sum

            

        return max_sum
        