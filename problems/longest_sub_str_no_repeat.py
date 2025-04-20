class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/6641428/o-n-solution-for-the-longest-substring-without-repeating-characters
        # In each iteration, we will find the longest string ending with that character
        # that has no duplicates. The character we are at is at r index. The max string that has no repeats could be 
        # l = 0. If we do find duplicates, we start increasing l until we have no duplicates. If we want to check the next
        # r character now, its l cannot be lower than the l from the previous iteration because if it is we will have a duplicate
        # with previous r
        
        l = 0
        longest = 0
        sset = set()
        for char in s:
            while char in sset:
                sset.remove(s[l])
                l+=1
            sset.add(char)
            if len(sset)>longest:
                longest = len(sset)
        return longest

            
                
        
            

s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
