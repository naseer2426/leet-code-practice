class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return ""
        
        str_num = str(num)
        ans = ""
        if str_num[0] != "9" and str_num[0] != "4":
            l = self.largest_num_that_can_sub(num)
            ans += self.simple_num_to_roman(l)
            ans += self.intToRoman(num-l)
        elif str_num[0] == "9":
            roman,n = self.get_9_special(num)
            ans+=roman
            ans += self.intToRoman(num-n)
        else:
            roman,n = self.get_4_special(num)
            print(roman,n)
            ans+=roman
            ans += self.intToRoman(num-n)

        return ans
    def largest_num_that_can_sub(self,num):
        choices = [1000,500,100,50,10,5,1]
        for choice in choices:
            if num-choice >= 0:
                return choice

    def get_9_special(self,n):
        if n < 10:
            return "IX",9
        elif n < 100:
            return "XC",90
        elif n < 1000:
            return "CM",900

    def get_4_special(self,n):
        if n < 5:
            return "IV",4
        elif n < 50:
            return "XL",40
        elif n < 500:
            return "CD",400
     
    def simple_num_to_roman(self,n):
        if n==1:
            return "I"
        elif n == 5:
            return "V"
        elif n == 10:
            return "X"
        elif n == 50:
            return "L"
        elif n ==100:
            return "C"
        elif n == 500:
            return "D"
        else:
            return "M"

s = Solution()
print(s.intToRoman(3749))
