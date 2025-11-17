class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        min_ts, _ = self.d[key][0]
        if timestamp < min_ts:
            return ""
        return self.bin_search(key, timestamp)
    
    def bin_search(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l+r)//2
            ts, val = arr[mid]
            if ts > timestamp:
                r=mid-1
                continue
            if ts == timestamp:
                return val
            if ts < timestamp and mid < len(arr) - 1 and timestamp < arr[mid+1][0]:
                return val
            l=mid+1
        
        return arr[-1][1] # since we only call this function when timestamp > min timestamp, the only case where we cannot find an answer is if timestamp > max timestamp
        
inp = ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
t = TimeMap()

i = 1
while i<len(inp):
    op = inp[i]
    if op == "set":
        t.set(inp[i+1][0],inp[i+1][1],inp[i+1][2])
        i+=2
        continue
    if op == "get":
        val = t.get(inp[i+1][0],inp[i+1][1])
        print(f"get {(inp[i+1][0],inp[i+1][1])} - {val}")
        i+=2
        continue
    i+=2
    print(f"invalid op {op}")
