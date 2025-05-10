class Solution:
    def partitions(self, n: int):
        stack = [[]]
        visited = {}
        all_depths = []

        while len(stack)!=0:
            curr = stack.pop(-1)
            if sum(curr) == n:
                all_depths.append(curr)
                continue
            if len(curr) == 8:
                continue
            for i in range(1,n+1):
                new = curr + [i]
                key = self.arr_key(new)
                if key in visited or sum(new)>n:
                    continue
                visited[key] = True
                stack.append(new) 
        
        return all_depths

    def arr_key(self,arr):
        k = ""
        for a in arr:
            k+=str(a)
        
        return k
        
    
s = Solution()
print(s.partitions(8))
