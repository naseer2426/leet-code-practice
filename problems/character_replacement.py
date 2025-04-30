class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  #using hash map to track freq of each char in s
        res = 0     #for returning maximum length of substring after performing operations
        
        l = 0
        maxFreq = 0
        for r in range(len(s)):
             #increasing freq of char at r index in hash map   
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]]) #calculating max freq (not scanning any list)

            #check if current window is valid
            # window length - maximum freq value from hash map <= k
            while (r - l + 1) - maxFreq > k: 
                count[s[l]] -= 1  #decrement freq of char at l in map
                l += 1            #shrink window size
            res = max(res, r - l + 1) #maximum value (size of the window, res)
        return res
s = Solution()
print(s.characterReplacement("BBBBAAAABAA",1))
