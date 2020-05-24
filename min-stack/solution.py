from bisect import insort

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_sort = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        insort(self.stack_sort, x)
        

    def pop(self) -> None:
        self.stack_sort.remove(self.stack.pop())
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack_sort[0]