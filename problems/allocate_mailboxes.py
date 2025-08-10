class Solution:
    def minDistance(self, houses,k):
        houses.sort()
        mem = {}
        return self.minDistanceWithK(houses, 0, len(houses),k, mem)

    def minDistanceWithK(self, houses, start,end, k, mem):
        #print(f"evaluating for {(start,end,k)}")
        if (start,end,k) in mem:
            return mem[(start,end,k)]
        if k >= len(houses[start:end]):
            mem[(start,end,k)] = 0
            return 0
        if k == 1:
            ans = self.minDistanceWithOne(houses, start,end,mem)
            mem[(start,end,k)] = ans
            #print(f"ans: {ans}")
            #print("---------------------")
            return ans
        if (start,end,k) not in mem:
            min_dist = self.minDistanceWithOne(houses, start, start+1, mem) + self.minDistanceWithK(houses, start+1, end, k-1, mem)
            for n in range(2,len(houses[start:end])):
                new_dist = self.minDistanceWithOne(houses, start, start+n,mem) + self.minDistanceWithK(houses, start+n,end,k-1, mem)
                min_dist = min(new_dist, min_dist)
            mem[(start,end,k)] = min_dist
        #print(f"ans: {mem[(start,end,k)]}")
        #print("---------------------")
        return mem[(start,end,k)]
        
        
    def minDistanceWithOne(self,houses, start,end, mem):
        if (start,end,1) in mem:
            return mem[(start,end,1)]
        size = len(houses[start:end])
        if size == 0:
            mem[(start,end,1)] = 0
            return 0
        mailbox_pos = houses[start+size//2]
        dist = 0
        for house in houses[start:end]:
            dist += abs(house-mailbox_pos)
        mem[(start,end,1)] = dist
        return mem[(start,end,1)]

s = Solution()
print(s.minDistance([1,8,12,10,3],3))
