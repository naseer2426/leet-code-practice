class Solution(object):
    def __init__(self):
        self.move_options = {
            "0":["1","9"],
            "1":["2","0"],
            "2":["1","3"],
            "3":["2","4"],
            "4":["5","3"],
            "5":["4","6"],
            "6":["5","7"],
            "7":["6","8"],
            "8":["7","9"],
            "9":["8","0"],
        }

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        
        deadend_set = set(deadends)
        if "0000" in deadends:
            return -1
        queue = [("0000",0)]
        visited = {}
        while len(queue) != 0:
            code, moves = queue.pop(0)
            if code == target:
                return moves
            
            visited[code] = True
            all_possible=self.all_possible_next(deadend_set,visited,code)
            for possible_code in all_possible:
                queue.append((possible_code,moves+1))
                visited[possible_code] = True
        
        return -1
    
    def all_possible_next(self, deadend_set,visited, curr_code):
        all_possible = []
        for i in range(len(curr_code)):
            curr_code_lst = list(curr_code)
            options = self.move_options[curr_code[i]]
            for option in options:
                curr_code_lst[i] = option
                code = "".join(curr_code_lst)
                if code in deadend_set or code in visited:
                    continue
                all_possible.append("".join(curr_code_lst))
        return all_possible


s = Solution()
# print(s.all_possible_next(['0100'],"0000"))
print(s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"],"8888"))
