class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:    
                target = nums[i] + nums[j] + nums[k]

                if target == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif target > 0:
                    k = k - 1
                else:
                    j = j + 1
                
        return res

        