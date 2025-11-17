class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i,h in enumerate(heights):
            if len(stack) == 0:
                stack.append((i,h))
                continue
            top_idx, top_h = stack[-1]
            if h >= top_h:
                stack.append((i,h))
                continue

            while h < top_h:
                max_area = max(max_area, (i-top_idx)*top_h)
                popped_idx, _ = stack.pop()
                if len(stack) == 0:
                    break
                top_idx, top_h = stack[-1]
            stack.append((popped_idx,h)) # popped_idx instead of curr idx because this h can be extended back until the point we popped because everything we popped was greater in height

        while len(stack) != 0:
            top_idx, top_h = stack.pop()
            max_area = max(max_area, (len(heights)-top_idx)*top_h)
        return max_area
s = Solution()
print(s.largestRectangleArea([7,1,7,2,2,4]))
