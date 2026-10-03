# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatten_list = []
        self.i = 0

        def flatten(nested_List):
            for item in nested_List:
                if item.isInteger():
                    self.flatten_list.append(item.getInteger())
                else:
                    flatten(item.getList())

        flatten(nestedList)

    def next(self) -> int:
        if self.i < len(self.flatten_list):
            val = self.flatten_list[self.i]
            self.i += 1
            return val
    
    def hasNext(self) -> bool:
        if self.i < len(self.flatten_list):
            return True
        else:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())