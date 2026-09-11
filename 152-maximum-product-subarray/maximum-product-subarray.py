class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_1, max_2 = float('-inf'), float('-inf')
        curr_prod_1, curr_prod_2 = 1, 1

        for i in range(n):
            curr_prod_1 *= nums[i]
            curr_prod_2 *= nums[n-i-1]
            max_1 = max(max_1, curr_prod_1)
            max_2 = max(max_2, curr_prod_2)

            if curr_prod_1 == 0:
                curr_prod_1 = 1
            if curr_prod_2 == 0:
                curr_prod_2 = 1
        
        return max(max_1, max_2)

        
        