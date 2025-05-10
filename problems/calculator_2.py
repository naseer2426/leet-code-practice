'''
My original intuition for this problem was using a binary tree to create the number operand number graph
But I found this making this graph in o(n) was pretty tricky, I could not find a good solution

One of the submitted solutions pointed out this really neat trick where we dont really need ot make a graph
but we can simply prioritize multiplication and division and do sum (and subtraction) at the end

The way we do this is maintaining a to_sum array where we add - values if the previous operator was -
if previous operator was / or * we immediately divide or multiply the current number with last number of to_sum array

Super nice trick!
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        to_sum = []
        parsed_s = self.parse(s)
        prev_operator = "+"
        for c in parsed_s:
            
            if not c.isdigit():
                prev_operator = c
                continue
            if prev_operator=="*":
                to_sum[-1]*=int(c)
                continue
            if prev_operator=="/":
                to_sum[-1]=int(to_sum[-1]/int(c))
                continue
            if prev_operator=="-":
                to_sum.append(-int(c))
                continue
            to_sum.append(int(c))
        return sum(to_sum)    

    def parse(self,s):
        p = []
        curr_num = ""
        for c in s:
            if c == " ":
                continue
            if not c.isdigit():
                if curr_num!="":
                    p.append(curr_num)
                    curr_num = ""
                p.append(c)
                continue
            curr_num+=c
        if curr_num!="":
            p.append(curr_num)
        return p
            

s = Solution()
print(s.calculate("14-3/2"))

        