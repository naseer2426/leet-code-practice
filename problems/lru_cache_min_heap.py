class MinHeap(object):
    def __init__(self):
        self.a = []
        self.key_to_idx = {}
    
    def get_min(self):
        return self.a[0] if len(self.a) >0 else None
    
    def insert_from_bottom(self,val):
        key, _ = val
        self.a.append(val)
        i = len(self.a) - 1
        self.key_to_idx[key] = i

        while i > 0 and self.a[(i-1)//2][1] > self.a[i][1]:
            self.swap((i-1)//2,i)
            i = (i-1)//2

    def delete_val_at_idx(self,idx):

        val = self.a[idx]
        self.swap(idx,len(self.a)-1)
        self.a = self.a[:-1]
        

        while idx < len(self.a):
            left_idx = 2*idx+1
            right_idx = 2*idx+2
            min_idx = idx

            if left_idx < len(self.a) and self.a[left_idx][1] < self.a[min_idx][1]:
                min_idx = left_idx
            if right_idx < len(self.a) and self.a[right_idx][1] < self.a[min_idx][1]:
                min_idx = right_idx
            if min_idx == idx:
                break
            self.swap(idx,min_idx)
            idx = min_idx
        
    def swap(self,i,j):
        self.a[i],self.a[j] = self.a[j],self.a[i]
        self.key_to_idx[self.a[i][0]] = i
        self.key_to_idx[self.a[j][0]] = j
    
    def delete_key(self,key):
        if key not in self.key_to_idx:
            return
        idx = self.key_to_idx[key]
        self.delete_val_at_idx(idx)
        del self.key_to_idx[key]

    def upsert_key(self,val):
        self.delete_key(val[0])
        self.insert_from_bottom(val)

class LRUCache(object):

    def __init__(self, capacity):
        self.operation_count = 0
        self.capacity= capacity
        self.map = {}
        self.curr_key_size = 0
        self.min_heap = MinHeap()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        self.operation_count+=1
        self.min_heap.upsert_key((key,self.operation_count))
        
        return self.map[key]

    def lru_key(self):
        key, _ = self.min_heap.get_min()
        return key

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.curr_key_size >= self.capacity and key not in self.map:
            lru_key = self.lru_key()
            del self.map[lru_key]
            self.min_heap.delete_key(lru_key)
            self.curr_key_size -= 1

        if key not in self.map:
            self.curr_key_size+=1
        self.map[key] = value
        self.operation_count+=1
        self.min_heap.upsert_key((key,self.operation_count))

def run_test_case(lst1,lst2):
    if len(lst1)!=len(lst2):
        print("wrong inputs")
        return
    cache = LRUCache(lst2[0][0])
    resp = ["null"]
    for i in range(1,len(lst1)):
        op = lst1[i]
        val = lst2[i]
        if op == "put":
            cache.put(val[0],val[1])
            resp.append("null")
            continue
        if op == "get":
            output = cache.get(val[0])
            resp.append(output)

    return resp

print(run_test_case(["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]))
