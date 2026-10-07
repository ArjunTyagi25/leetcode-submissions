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

            for time, value in reversed(values):
                if time <= timestamp:
                    return value
            return ""
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)