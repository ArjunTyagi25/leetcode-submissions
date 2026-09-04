class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(m):
            left = 0
            count = defaultdict(int)
            total = 0

            if m == 0:
                return total

            for right in range(len(nums)):
                # Increment the count of the newly encountered value that is nums[right]
                count[nums[right]] += 1

                # Check if the size of hash map is greater than k. If so, shrink window till it is not.
                while len(count) > m:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1

                # Increment the res with the number of subarrays starting at left or beyond and ending at right
                total += right - left + 1
            return total

        return atMost(k) - atMost(k-1)
                
