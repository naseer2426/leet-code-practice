class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq_dict = {}
        for c in s1:
            if c not in s1_freq_dict:
                s1_freq_dict[c] = 0
            s1_freq_dict[c]+=1

        #print(s1_freq_dict)
        s1_l = len(s1)
        s2_sub_freq_dict = {}
        for i in range(s1_l):
            c = s2[i]
            if c not in s2_sub_freq_dict:
                s2_sub_freq_dict[c] = 0
            s2_sub_freq_dict[c]+=1
        #print(s2_sub_freq_dict)
        if self.d1_in_d2(s1_freq_dict,s2_sub_freq_dict):
            return True
        l = 0
        r = s1_l

        while r < len(s2):
            if s2[r] not in s2_sub_freq_dict:
                s2_sub_freq_dict[s2[r]] = 0
            s2_sub_freq_dict[s2[r]]+=1
            s2_sub_freq_dict[s2[l]]-=1
            #print(f"d1 - {s1_freq_dict}, d2 - {s2_sub_freq_dict}")
            if self.d1_in_d2(s1_freq_dict,s2_sub_freq_dict):
                return True
            r+=1
            l+=1
        return False

    def d1_in_d2(self, d1, d2):
        for k in d1:
            if k not in d2:
                return False
            if d1[k] > d2[k]:
                return False
        return True

s = Solution()
#print(s.checkInclusion("ab","lecabee"))
