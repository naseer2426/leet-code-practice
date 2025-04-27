class MinHeap:
    def __init__(self,max_size):
        self.a = []
        self.max_size = max_size
    def insert_from_end(self,val):
        '''
        For an array representation of a binary try, for any given index i
        parent idx = (i-1)//2
        left child idx = 2*i+1
        right child idx = 2*i+2
        '''
        self.a.append(val)
        i = len(self.a) - 1

        while i>0 and self.a[(i-1)//2] > self.a[i]:
            self.a[i],self.a[(i-1//2)] =  self.a[(i-1//2)],self.a[i]
            i = (i-1)//2

        self.a = self.a[:self.max_size]
    
    def relace_min(self,val):
        self.a[0] = val
        i = 0
        while i < len(self.a):
            left = 2*i+1
            right = 2*i+2
            min_idx = i
            if left < len(self.a) and self.a[left] < self.a[min_idx]:
                min_idx = left
            if right < len(self.a) and self.a[right] < self.a[min_idx]:
                min_idx = right
            if min_idx == i:
                break
            self.a[min_idx], self.a[i] = self.a[i], self.a[min_idx]
            i = min_idx


    def get_min(self):
        return self.a[0] if len(self.a) > 0 else None
 


lst = [5,6,8,7,9,35,1,-3]
m = MinHeap(3)

for i in range(3):
    m.insert_from_end(lst[i])

for l in lst:
    if m.get_min() != None and l > m.get_min():
        m.relace_min(l)

print(m.a)
