class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        elif val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
        self.stack.pop()

    # def pop(self) -> None:
    #     self.stack.pop()
    #     if self.minStack and self.minStack[-1] == self.stack[-1]:
    #         self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return 0
