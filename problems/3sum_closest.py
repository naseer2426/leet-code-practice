class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        res = nums[0]+nums[1]+nums[2]
        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = l-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target-s) < abs(target-res):
                    res = s
                if s < target:
                    left+=1
                elif s > target:
                    right-=1
                else:
                    return target
        return res
    
s = Solution()
print(s.threeSumClosest([0,0,0],1))
