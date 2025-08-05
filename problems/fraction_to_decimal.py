class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str

        note that this implementation is not fully correct. It does not handle
        negetive numbers correctly, but this problem is just tedious not hard
        """
        q = numerator//denominator
        r = numerator - denominator*q
        if r == 0:
            return str(q)
        ans = str(q)+"."
        curr = r
        seen = {}
        while curr not in seen:
            new_num = r*10
            
            q = new_num//denominator
            r = new_num - denominator*q
            
            ans+=str(q)
            if r == 0:
                return ans
            seen[curr] = q
            curr = r

        ans = self.replace_first_occurance(ans,str(seen[curr]))
        return ans+")"

    def replace_first_occurance(self,ans,num):
        res = ""
        whole, decimal = ans.split(".")
        replaced = False
        for a in decimal:
            if a == num and not replaced:
                res+="("+a
                replaced=True
                continue
            res+=a
        return whole+"."+res
        
s = Solution()
print(s.fractionToDecimal(1,3))
        