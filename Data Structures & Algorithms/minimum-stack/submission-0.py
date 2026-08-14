class MinStack:

    def __init__(self):
        self.stack = list()
        self.mono_stack = list()
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.mono_stack and val > self.mono_stack[-1]:
            return
        self.mono_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # check if min ele is the one popped, if the numbers are repeated we might need to check for index
        if val == self.mono_stack[-1]:
            self.mono_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else 0

    def getMin(self) -> int:
        return self.mono_stack[-1]
        
