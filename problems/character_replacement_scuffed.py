'''
My solution to this problem keeps track of the highest frequnce letter in the substring
using a max heap. This solution intuitively made sense to me but apparently its wrong.

There is a simpler solution where you dont need to track the highest frequence character in
the sub string. You only need to track the highest frequency character in any substring
evaluated till now and the algorithm works perfectly fine

I HAVE NO IDEA WHY IT WORKS BUT IT DOES. what makes it worse is that my solution fails some 
test cases on leetcode. I hate leetcodeing with a passion.

check character_replacement.py for correct solution >:(
'''

class MaxHeap:
    def __init__(self):
        self.a = []
        self.idx_map = {}
    
    def max_value(self):
        return self.a[0] if len(self.a)>0 else None
    
    def insert_from_bottom(self, val):
        self.a.append(val)
        i = len(self.a) - 1
        while i > 0 and self.a[(i-1)//2][1] < self.a[i][1]:
            self.a[(i-1)//2], self.a[i] = self.a[i], self.a[(i-1)//2]
            self.idx_map[self.a[i][0]] = i
            i = (i-1)//2
        self.idx_map[val[0]] = i

    def down(self,from_idx):
        i = from_idx
        while i < len(self.a):

            left = 2*i + 1
            right = 2*i + 2
            max_idx = i

            if left < len(self.a) and self.a[left] > self.a[max_idx]:
                max_idx = left
            if right < len(self.a) and self.a[right] > self.a[max_idx]:
                max_idx = right
            if max_idx == i:
                break
            self.a[i], self.a[max_idx] = self.a[max_idx], self.a[i]
            self.idx_map[self.a[i][0]] = i
            i = max_idx
        
    def delete(self,val):
        if val[0] not in self.idx_map:
            return
        val_idx=self.idx_map[val[0]]
        del self.idx_map[val[0]]
        self.a[val_idx],self.a[len(self.a)-1]=self.a[len(self.a)-1],self.a[val_idx]
        self.idx_map[self.a[val_idx][0]] = val_idx
        self.a = self.a[0:-1]
        self.down(val_idx)

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0:
            return 0
        l = 0
        longest = -1
        freq_map = {s[0]:1}
        max_heap = MaxHeap()
        max_heap.insert_from_bottom((s[0],1))

        for r in range(1,len(s)):
            if s[r] not in freq_map:
                freq_map[s[r]] = 0
            freq_map[s[r]]+=1
            # max_heap.delete(s[r])
            max_heap.insert_from_bottom((s[r],freq_map[s[r]]))
            _,max_freq = max_heap.max_value()
            while (r-l+1) - max_freq > k:
                freq_map[s[l]]-=1
                max_heap.delete(s[l])
                max_heap.insert_from_bottom(((s[l]),freq_map[s[l]]))
                l+=1
                _,max_freq = max_heap.max_value()
            if r==71:
                print(s[l:r+1],(l,r))
            if r-l+1 > longest:
                longest = r-l+1
                if longest == 15:
                    ans = s[l:r+1]
                    print(ans,len(ans),(l,r))
                    fm ={}
                    for c in ans:
                        if c not in fm:
                            fm[c] = 0
                        fm[c]+=1
                    print(fm)
        return longest
    
s = Solution()
print(s.characterReplacement("BRJRRKNRBFOOKDEEGODTGMHNABMTHFNPTFRHRSEKKTFEQIKSIAJJMSDSLNSCNRNJFNFSIQDNMHDRIJIACLCJKATTFHDASGLRQSFN",10))



