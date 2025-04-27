class MinHeapBounded(object):
        def __init__(self,max_size):
            self.a = []
            self.max_size = max_size
        
        def insert_from_bottom(self, val):
            self.a.append(val)
            i = len(self.a) - 1

            while i > 0 and self.a[(i-1)//2][1] > self.a[i][1]:
                self.a[(i-1)//2], self.a[i] = self.a[i], self.a[(i-1)//2]
                i = (i-1)//2
            self.a = self.a[:self.max_size]

        def replace_min(self,val):
            if len(self.a) == 0:
                self.insert_from_bottom(val)
                return
            self.a[0] = val
            i = 0
            while i < len(self.a):
                left_idx = 2*i + 1
                right_idx = 2*i + 2

                min_idx = i

                if left_idx < len(self.a) and self.a[left_idx][1] < self.a[min_idx][1]:
                    min_idx = left_idx
                if right_idx < len(self.a) and self.a[right_idx][1] < self.a[min_idx][1]:
                    min_idx = right_idx
                if min_idx == i:
                    break
                self.a[min_idx],self.a[i] = self.a[i], self.a[min_idx]
                i = min_idx

        def get_min(self):
            return self.a[0] if len(self.a) > 0 else None

class Solution(object):
        
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 0
            freq_dict[num]+=1

        unique_nums = list(freq_dict.keys())
        m = MinHeapBounded(k)
        for i in range(k):
            m.insert_from_bottom((unique_nums[i],freq_dict[unique_nums[i]]))
        
        for i in range(k,len(unique_nums)):
            freq = freq_dict[unique_nums[i]]
            min_of_max_k, freq_min_of_max_k = m.get_min()
            
            if freq > freq_min_of_max_k:
                m.replace_min((unique_nums[i],freq))
        
        res = []
        for item in m.a:
            res.append(item[0])
        return res
    
s = Solution()
print(s.topKFrequent([6,0,1,4,9,7,-3,1,-4,-8,4,-7,-3,3,2,-3,9,5,-4,0],6))
