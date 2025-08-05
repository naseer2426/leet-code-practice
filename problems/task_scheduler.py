class Solution:
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)
        if len(tasks) == 0:
            return 0

        freq_dict = {}
        total_tasks = 0
        for task in tasks:
            if task not in freq_dict:
                freq_dict[task] = 0
            freq_dict[task]+=1
            total_tasks+=1
        
        last_exec = {}
        cycle = 0
        while total_tasks!=0:
            available = self.available_task(freq_dict,last_exec,cycle,n)
            if available==None:
                cycle+=1
                # print("idle")
                continue
            # print(available)
            freq_dict[available]-=1
            last_exec[available] = cycle
            total_tasks-=1
            cycle+=1

        return cycle
    
    def available_task(self,freq_dict,last_exec_cycle, curr_cycle, n):
        highest_freq_task = ""
        highest_freq = 0
        for task in freq_dict:
            if freq_dict[task] == 0:
                continue
            if task in last_exec_cycle and curr_cycle - last_exec_cycle[task] <= n:
                continue
            freq = freq_dict[task]
            if freq > highest_freq:
                highest_freq = freq
                highest_freq_task = task
        if highest_freq_task == "":
            return None
        return highest_freq_task
            


s = Solution()
print(s.leastInterval(["B","C","D","A","A","A","A","G"],1))
