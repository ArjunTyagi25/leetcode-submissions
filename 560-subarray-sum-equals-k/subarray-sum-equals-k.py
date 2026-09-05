class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_of_seen_prefixs = {0 : 1}
        res = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            past_prefix = curr_sum - k

            if past_prefix in freq_of_seen_prefixs:
                res += freq_of_seen_prefixs[past_prefix]

            freq_of_seen_prefixs[curr_sum] = 1 + freq_of_seen_prefixs.get(curr_sum, 0)

        return res

        