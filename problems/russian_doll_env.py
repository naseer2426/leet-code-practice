class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(reverse=True)
        mem = {}
        max_env = 0
        for i in range(len(envelopes)):
            max_env = max(max_env,self.russianDoll(i,envelopes,mem))
            print(f"i {i} - max_env {max_env}")
        return max_env
    
    def russianDoll(self,i, envolopes, mem):
        if i in mem:
            return mem[i]
        if i == len(envolopes)-1:
            mem[i] = 1
            return mem[i]
        env = envolopes[i]
        max_env = 1
        for e in range(i,len(envolopes)):
            if envolopes[e][0] < env[0] and envolopes[e][1] < env[1]:
                max_env = max(max_env,self.russianDoll(e,envolopes,mem)+1)
        mem[i] = max_env
        return mem[i]

s = Solution()
print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
