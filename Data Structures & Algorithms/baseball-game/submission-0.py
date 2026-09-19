class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                m1,m2 = stack[-1], stack[-2]
                stack.append((int(m1)+int(m2)))
            elif op == "D":
                m1 = stack[-1]
                stack.append((int(m1)*2))
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)