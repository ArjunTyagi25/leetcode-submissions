class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[timestamp, value]]
        else:
            self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            values = self.map[key]

            L, R = 0, len(values) - 1
            res = ""

            while L<=R:
                M = (L+R)//2

                if values[M][0] <= timestamp:
                    res = values[M][1]
                    L = M + 1
                else:
                    R = M - 1

            return res
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)