class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        height = min(2 chosen poles)
        base = (difference between indexes of poles)
        To maximize -> height * base

        Greedy approach wins here. The inituition I had thought of first is that considering a given choice of poles, for the smaller one, the 
        the other pole that maximises water is the farthest away pole which is greater than or equal to its size

        We start with the largest possible base which is start idx and end idx lets call it b. We greedily make choices for 
        b-1 by moving the pointer with lower height ahead, because moving the pointer with higher height will always lead in a smaller area

        How this strategy links to my initial intuition is that among the 2 chose poles, considering we start with highest possible base,
        this will be the highest area for the smaller pole (because as we continue iterating, the base will decrease and height cannot be higher than current height)

        That means in each iteration we would have considered the largest possible area we can make with the smaller pole.

        Let s, l be the indexes of the 2 poles which maximize area, where height[s] < height[l], this algorithm will find l when the 2 poles its comparing is
        contains s 
        """
        if len(height) < 3:
            return min(height)

        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right-left)
            if area > max_area:
                max_area = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
