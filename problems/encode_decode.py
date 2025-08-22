class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            l = len(s)
            res+=str(l)+")"
            res+=s
        return res

    def decode(self, s):
        i = 0
        res = []
        while i<len(s):
            end_idx = i+s[i:].find(")")
            l = int(s[i:end_idx])
            res.append(s[end_idx+1:end_idx+1+l])
            i = end_idx+1+l
        return res

s = Solution()
e = s.encode(["neet","code","love","you"])
print(e)
print(s.decode(e))
