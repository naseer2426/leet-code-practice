class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        lower_limit = -2**31
        upper_limit = 2**31-1

        trimmed_white_spaces = s.strip()
        if trimmed_white_spaces == "":
            return 0
        is_postive = self.is_positive(trimmed_white_spaces)
        trimmed = self.trim(trimmed_white_spaces)
        converted = self.convert_to_pos_int(trimmed)


        if not is_postive:
            _converted = -1*converted
            if lower_limit <= _converted:
                return -1*converted
            return lower_limit
        elif converted > upper_limit:
            return upper_limit
        return converted

    def convert_to_pos_int(self, s):
        ans = 0
        for i in range(len(s)):
            p = len(s) - i - 1
            ans += self.conv_digit(s[i])*10**p
        return ans


    def conv_digit(self, c):
        if c == "0":
            return 0
        elif c == "1":
            return 1
        elif c == "2":
            return 2
        elif c == "3":
            return 3
        elif c == "4":
            return 4
        elif c == "5":
            return 5
        elif c == "6":
            return 6
        elif c == "7":
            return 7
        elif c == "8":
            return 8
        elif c == "9":
            return 9
        else:
            return 0

    
    def is_positive(self,s):
        if s[0] == "-":
            return False
        return True

    def trim(self, s):
        start_idx = 0
        end_idx = len(s)

        _s = s
        if (_s[0] == "-" or _s[0] == "+"):
            _s = _s[1:]
        
        for i in range(len(_s)):
            if s[i] == "0":
                continue
            start_idx = i
            break
        
        for i in range(start_idx, len(_s)):
            if _s[i].isdigit():
                continue
            end_idx = i
            break
        return _s[start_idx:end_idx]

s = Solution()
print(s.myAtoi("+1"))
