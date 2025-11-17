class Solution:
    def evalRPN(self, tokens):
        symbols = ['+','-','*','/']
        stack = []
        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
                continue
            op2 = stack.pop()
            op1 = stack.pop()
            if token == "+":
                stack.append(op1+op2)
            if token == "-":
                stack.append(op1-op2)
            if token == "*":
                stack.append(op1*op2)
            if token == "/":
                stack.append(op1/op2)
        return stack[-1]

s = Solution()
print(s.evalRPN(["4","13","5","/","+"]))

k = [3,6,3,5,7,8,9,0,3,4] 
