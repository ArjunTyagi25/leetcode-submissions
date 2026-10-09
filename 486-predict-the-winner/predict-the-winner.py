class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        numsQueue = deque(nums)

        def rec(player1Score, player2Score, turn):
            if not numsQueue:
                if player1Score >= player2Score:
                    return True
                else:
                    return False

            if turn == "player1":
                firstNum = numsQueue.popleft()
                player1Score += firstNum
                res_1 = rec(player1Score, player2Score, "player2")
                player1Score -= firstNum
                numsQueue.appendleft(firstNum)

                lastNum = numsQueue.pop()
                player1Score += lastNum
                res_2 = rec(player1Score, player2Score, "player2")
                player1Score -= lastNum
                numsQueue.append(lastNum)

                return res_1 or res_2
            else:
                firstNum = numsQueue.popleft()
                player2Score += firstNum
                res_1 = rec(player1Score, player2Score, "player1")
                player2Score -= firstNum
                numsQueue.appendleft(firstNum)

                lastNum = numsQueue.pop()
                player2Score += lastNum
                res_2 = rec(player1Score, player2Score, "player1")
                player2Score -= lastNum
                numsQueue.append(lastNum)

                return res_1 and res_2

        return rec(0, 0, "player1")