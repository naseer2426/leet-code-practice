class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        self.letter_dict = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        combinations = []
        self.dfs(combinations,0,[],digits)
        
        return combinations
    

    def dfs(self,combinations, curr_idx, path, digits):
        if curr_idx == len(digits):
            combinations.append("".join(path))
            return
        for char in self.letter_dict[digits[curr_idx]]:
            path.append(char)
            self.dfs(combinations,curr_idx+1,path,digits)
            path.pop()
        


s = Solution()
print(s.letterCombinations("234"))
        
