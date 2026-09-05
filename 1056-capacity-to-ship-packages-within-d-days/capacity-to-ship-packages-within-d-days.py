class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L, R = max(weights), sum(weights)

        while L<R:
            max_capacity = (L+R)//2

            time = 1
            curr_total_weight = 0
            for w in weights:
                if curr_total_weight + w > max_capacity:
                    time += 1
                    curr_total_weight = w
                else:
                    curr_total_weight += w

            if time > days:
                L = max_capacity + 1
            else:
                R = max_capacity

        return L

        