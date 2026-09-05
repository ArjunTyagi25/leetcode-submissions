class Solution:

    def __init__(self, nums: List[int]):
        self.val_to_indices = {}
        
        for i in range(len(nums)):
            if nums[i] in self.val_to_indices:
                self.val_to_indices[nums[i]].append(i)
            else:
                self.val_to_indices[nums[i]] = [i]

    def pick(self, target: int) -> int:
        indices = self.val_to_indices[target]

        return random.choice(indices)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)