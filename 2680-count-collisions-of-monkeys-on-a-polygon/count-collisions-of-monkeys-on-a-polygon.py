class Solution:
    def monkeyMove(self, n: int) -> int:
        MAX = pow(10, 9) + 7
        return (pow(2, n, MAX) - 2) % MAX