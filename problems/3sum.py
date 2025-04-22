class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        valid_sets = []
        for i in range(l):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = l-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left+=1
                elif s > 0:
                    right-=1
                else:
                    valid_sets.append([nums[i] ,nums[left] ,nums[right]])
                    left+=1
                    while left < l and nums[left] == nums[left-1]:
                        left+=1
        return valid_sets

s = Solution()
print(s.threeSum([0,0,0]))
