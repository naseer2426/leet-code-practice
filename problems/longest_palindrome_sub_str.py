class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #https://leetcode.com/problems/longest-palindromic-substring/solutions/6641468/longest-palindromic-substring
        if s == "":
            return ""
        start = 0
        max_len = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len=r-l+1
                    start = l
                l=l-1
                r=r+1
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len=r-l+1
                    start = l
                l=l-1
                r=r+1
        return s[start:start+max_len]

s = Solution()
print(s.longestPalindrome("babad"))
