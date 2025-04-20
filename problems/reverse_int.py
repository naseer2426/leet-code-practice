class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lower_limit = str(-2**31)
        upper_limit = str(2**31-1)

        is_positive = abs(x) == x 

        str_int = str(abs(x))
        rev_str = str_int[::-1]
        
        if is_positive and self.less_than_equal(rev_str,upper_limit):
            return int(rev_str)
        elif not is_positive and not self.less_than_equal(lower_limit,"-"+rev_str):
            return int("-"+rev_str)
        return 0
    
    def less_than_equal(self,num1,num2):
        if (num1==num2):
            return True
        if len(num1) < len(num2):
            return True
        if len(num2) < len(num1):
            return False
        return self.remove_preceding_zeros(num1) < self.remove_preceding_zeros(num2)
        
    def remove_preceding_zeros(self,num):
        for i in range(len(num)):
            c = num[i]
            if  c == "0":
                continue
            return num[i:]
        return "0"

s = Solution()
print(s.reverse(-123))
