# https://leetcode.com/problems/flatten-nested-list-iterator/?envType=daily-question&envId=2023-10-20 

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
        list = []
        def fillList(nestedList: [NestedInteger]):
            for node in nestedList:
                if node.isInteger():
                    list.append(node.getInteger())
                else:
                    fillList(node.getList())
        fillList(nestedList)
        self.l = list
        self.curInx = 0
    
    def next(self) -> int:
        val = self.l[self.curInx]
        self.curInx += 1
        return val
    
    def hasNext(self) -> bool:
         return self.curInx < len(self.l)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
