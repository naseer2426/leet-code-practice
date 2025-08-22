class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        res = []
        for k in groups.keys():
            res.append(groups[k])
        return res

s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
