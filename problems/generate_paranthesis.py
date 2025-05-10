class Solution:
    def generateParenthesis(self, n):
        valid = []
        stack = [("",0,0)]
        visited = {}
        while len(stack)!=0:
            paranthesis_str,left_count,right_count = stack.pop(-1)
            if left_count == right_count and right_count == n:
                valid.append(paranthesis_str)
                continue
            if left_count < n:
                new_p_str = paranthesis_str+"("
                if new_p_str not in visited:
                    stack.append((new_p_str,left_count+1,right_count))
                    visited[new_p_str] = True
            if right_count < left_count and right_count < n:
                new_p_str = paranthesis_str+")"
                if new_p_str not in visited:
                    stack.append((new_p_str,left_count,right_count+1))
                    visited[new_p_str] = True
        return valid


s = Solution()
print(s.generateParenthesis(8))
