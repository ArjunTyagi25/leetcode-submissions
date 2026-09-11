class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        window = {}
        L = 0

        for R in range(len(fruits)):
            fruit = fruits[R]
            window[fruit] = 1 + window.get(fruit, 0)

            while len(window) > 2:
                window[fruits[L]] -= 1

                if window[fruits[L]] == 0:
                    del window[fruits[L]]

                L += 1

            res = max(res, R - L + 1)

        return res
            
        