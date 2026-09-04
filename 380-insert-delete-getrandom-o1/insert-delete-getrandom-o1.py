class RandomizedSet:

    def __init__(self):
        self.values = []
        self.map = {}
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.values.append(val)
        self.map[val] = len(self.values)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index_of_val_remove = self.map[val]
        t = self.values[-1]
        self.values[-1] = val
        self.values[index_of_val_remove] = t

        self.map[t] = index_of_val_remove
        self.values.pop()
        del self.map[val]
        return True
        

    def getRandom(self) -> int:
        val_to_return = random.choice(self.values)

        return val_to_return
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()