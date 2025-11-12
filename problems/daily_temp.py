class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        ans = [0 for _ in range(len(temperatures))]
        for i,temp in enumerate(temperatures):
            while len(stack) > 0:
                peak_idx = stack[-1]
                peak_value = temperatures[peak_idx]
                if temp > peak_value:
                    ans[peak_idx] = i-peak_idx
                    stack.pop()
                else:
                    break
            stack.append(i)

        for remaining in stack:
            ans[remaining] = 0
        return ans

s = Solution()
print(s.dailyTemperatures([30,40,50,60]))
        