class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            creationTime = self.tokens[tokenId]

            if creationTime + self.timeToLive > currentTime:
                self.tokens[tokenId] = currentTime
            else:
                del self.tokens[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0

        for tokenId, creationTime in self.tokens.items():
            if creationTime + self.timeToLive > currentTime:
                res += 1

        return res


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)