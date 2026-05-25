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
                    res = int(n2 / n1)

                        
                elif n == "*":
                    res = n2 * n1
                stack.append(res)
            else:
                stack.append(int(n))      
        return(stack[0])