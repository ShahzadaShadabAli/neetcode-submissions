class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ["+", "/", "-", "*"]
        for n in tokens:
            if n in symbols:
                n1 = stack.pop()
                n2 = stack.pop()
                if n == "+":
                    res = n2 + n1     
                elif n == "-":
                    res = n2 - n1
                elif n == "/":
                    this = (n2 / n1)
                    if this < 0:
                        res = math.ceil(n2 / n1)
                    else:
                        res = math.floor(n2 / n1)

                        
                elif n == "*":
                    res = n2 * n1
                stack.append(res)
            else:
                stack.append(int(n))      
            print(stack)
        return(stack[0])