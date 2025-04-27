class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        queue = [[]]
        combinations = []
        visited = {}
        while len(queue) != 0:
            curr_candidates = queue.pop(0)
            if sum(curr_candidates) == target:
                combinations.append(curr_candidates)
            all_possible = self.all_possible_next(curr_candidates,candidates,target)
            for next_candidates in all_possible:
                key = str(next_candidates)
                if key in visited:
                    continue
                queue.append(next_candidates)
                visited[key] = True
            
        return combinations

    def all_possible_next(self, curr_candidates, candidates, target):
        curr_sum = sum(curr_candidates)
        res = []
        for candidate in candidates:
            if curr_sum+candidate >target:
                continue
            new_candidates = curr_candidates + [candidate]
            new_candidates.sort()
            res.append(new_candidates)
        return res

s = Solution()
print(s.combinationSum([2,3,6,7],7))
