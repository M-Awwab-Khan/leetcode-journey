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
        self.iterator = self.flatten(nestedList)
        self.next_element = None
        self._advance()
    
    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration()
        current_element = self.next_element
        self._advance()
        return current_element
    
    def _advance(self):
        try:
            self.next_element = next(self.iterator)
        except StopIteration:
            self.next_element = None

    def flatten(self, nestedList):
        for nested in nestedList:
            if nested.isInteger():
                yield nested.getInteger()
            else:
                yield from self.flatten(nested.getList())
    
    def hasNext(self) -> bool:
        return self.next_element is not None

# Example usage:
# Assuming NestedInteger is implemented and nestedList is given
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
