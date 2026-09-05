class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        curr_sum = 0

        for i in w:
            curr_sum += i
            self.prefix.append(curr_sum)

    def pickIndex(self) -> int:
        random_num = random.randint(1, self.prefix[-1])

        L, R = 0, len(self.prefix) - 1
        while L<R:
            M = (L+R)//2

            if self.prefix[M] < random_num:
                L = M + 1
            else:
                R = M
        
        return L
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()