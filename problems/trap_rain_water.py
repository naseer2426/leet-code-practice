class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        The intuition for this problem is that we can calculate the height of the water that will be trapped at each
        idx by knowing the heights of the max walls on the left and right of the index (including the idx). 
        Lets call them L, R

        The water that will be trapped here = min(L,R) - height[i] (notice height at i cannot be greater than min(L,R))
        A naive approach is to create 2 new arrays, on called maxL and other called maxR, where each idx represents the
        max wall on the left and right of that indx respectively. Creating these 2 arrays is a o(n) operation. Then
        finding min(L,R) - height[i] is a o(1) operation, which we simply sum at each idx. Hence for this naive approach
        Time complexity: O(n)
        Space complexity O(n)

        A better approach here comes from the understanding that at any given index we only need the MIN of both sides
        not both. This can be very efficiently calculated using 2 pointers. Initialize both pointers at both ends of the
        array. Then only focus on the one that is lower and calculate its water trapped, then move that pointer ahead and
        keep doing the same, until the other pointer becomes lower. The move this other pointer until both pointers meet
        """

        left_max, right_max = height[0], height[-1]
        l,r = 0, len(height)-1
        trapped = 0

        while l<=r:
            if left_max <= right_max:
                curr = height[l]
                if curr > left_max:
                    left_max = curr
                trapped+=left_max-curr
                # print(f"added {left_max-curr} water at idx {l}")
                l+=1
            if right_max < left_max:
                curr = height[r]
                if curr > right_max:
                    right_max = curr
                trapped += right_max - curr
                # print(f"added {right_max - curr} water at idx {r}")
                r-=1
        return trapped

s = Solution()
print(s.trap([5,5,1,7,1,1,5,2,7,6]))
