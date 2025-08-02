class MedianFinder(object):

    def __init__(self):
       self.left_half = MaxHeap()
       self.right_half = MinHeap()
       self.middle = None
       self.is_even_size = True

    def addNum(self, num):
        #print("addnum", num)
        if self.is_even_size:
            left_max = self.left_half.max()
            right_min = self.right_half.min()
            #print("left max", left_max)
            #print("right min", right_min)
            if (num > left_max and num < right_min) or (num == left_max) or (num==right_min):
                self.middle = num
            elif num < left_max:
                self.middle = self.left_half.pop_max()
                self.left_half.add_from_bottom(num)
            elif num > right_min:
                self.middle = self.right_half.pop_min()
                self.right_half.add_from_bottom(num)
            self.is_even_size = False
        else:
            left_max = self.left_half.max()
            right_min = self.right_half.min()
            curr_middle = self.middle
            self.middle = None

            if num <= curr_middle:
                self.left_half.add_from_bottom(num)
                self.right_half.add_from_bottom(curr_middle)
            elif num > curr_middle:
                self.right_half.add_from_bottom(num)
                self.left_half.add_from_bottom(curr_middle)
            self.is_even_size = True
        #print("left", self.left_half.a)
        #print("right",self.right_half.a)
        #print("middle", self.middle)
        #print("-------------------------------")
        #print()

    def findMedian(self):
        #print("findMedian")
        if self.middle!=None:
            return self.middle
        return (self.left_half.max()+self.right_half.min())/2

class MinHeap:
    def __init__(self):
        self.a = []

    def add_from_bottom(self,elem):
        self.a.append(elem)
        idx = len(self.a) - 1

        while idx > 0 and self.a[(idx-1)//2] > self.a[idx]:
            self.a[(idx-1)//2],self.a[idx] = self.a[idx], self.a[(idx-1)//2]
            idx = (idx-1)//2
        
    def pop_min(self):
        if len(self.a) == 0:
            return self.min()
        m = self.a[0]
        last_elem = self.a[-1]
        self.a[0] = last_elem
        self.a.pop()
        idx = 0
        while idx < len(self.a):
            left_idx = idx*2+1
            right_idx = idx*2+2
            min_idx = idx

            if left_idx < len(self.a) and self.a[left_idx] < self.a[min_idx]:
                min_idx = left_idx
            if right_idx < len(self.a) and self.a[right_idx] < self.a[min_idx]:
                min_idx = right_idx
            if min_idx == idx:
                break
            
            self.a[idx],self.a[min_idx] = self.a[min_idx],self.a[idx]
            idx = min_idx
        return m
    def min(self):
        if len(self.a) ==0:
            return 10**6
        return self.a[0]
    

class MaxHeap:
    def __init__(self):
        self.a = []

    def add_from_bottom(self,elem):
        self.a.append(elem)
        idx = len(self.a) - 1

        while idx > 0 and self.a[(idx-1)//2] < self.a[idx]:
            self.a[(idx-1)//2],self.a[idx] = self.a[idx], self.a[(idx-1)//2]
            idx = (idx-1)//2
        
    def pop_max(self):
        if len(self.a) == 0:
            return self.max()
        m = self.a[0]
        last_elem = self.a[-1]
        self.a[0] = last_elem
        self.a.pop()
        idx = 0
        while idx < len(self.a):
            left_idx = idx*2+1
            right_idx = idx*2+2
            max_idx = idx

            if left_idx < len(self.a) and self.a[left_idx] > self.a[max_idx]:
                max_idx = left_idx
            if right_idx < len(self.a) and self.a[right_idx] > self.a[max_idx]:
                max_idx = right_idx
            if max_idx == idx:
                break
            
            self.a[idx],self.a[max_idx] = self.a[max_idx],self.a[idx]
            idx = max_idx
        return m
    
    def max(self):
        if len(self.a) == 0:
            return -10**6
        return self.a[0]

def test(op_arr, val_arr):
    m = MedianFinder()
    res = ["null"]
    for i in range(1,len(op_arr)):
        op = op_arr[i]
        if op == "addNum":
            val = val_arr[i][0]
            m.addNum(val)
            res.append("null")
            continue
        if op == "findMedian":
            med = m.findMedian()
            res.append(med)
            #print("findMedian",med)
            #print("-------------------------------")
            #print()
            continue
    return res

#print(test(["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"],[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]))
