class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []
        self.counter = 0

    def push(self, val: int) -> None:
        self.counter+=1
        if len(self.mini) == 0:
            self.mini.append(val)
        else: 
            if self.mini[-1] > val:
                self.mini.append(val)
            else:
                self.mini.append(self.mini[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.mini.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
