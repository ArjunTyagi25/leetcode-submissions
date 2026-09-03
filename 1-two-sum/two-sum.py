class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}

        for i in range(len(nums)):
            curr = nums[i]
            x = target - curr
            if (x in value_to_index):
                return [value_to_index[x], i]
            else:
                value_to_index[curr] = i
        
        return [] 
        