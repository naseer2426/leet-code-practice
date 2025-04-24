class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        '''
        Key insight here is the intuition behind skipping the loop. For the first_idx after processing the first iteration
        if we see the same number again lets say a, 3 things can happen

            1. In the old iteration we never found a quadruplet including a which adds upto target
            2. We did find a quadruplet that adds upto target, which includes 2 copies of a (1 from first iteration) and
              another a from this iteration
            3. We did find a quadruplet that adds upto target, which includes 3 other numbers far awar from this number

        In all 3 cases above it does not make sense to process this loop where we see a again

            1. We will not find a quadruplet again
            2. If there exists another copy of a down the line, we wil find the same quadruplet again
            3. We will find the same quadruplet again
            
        '''
        nums.sort()
        quadruplets = []
        for first_idx in range(len(nums)):
            if first_idx>0 and nums[first_idx] == nums[first_idx-1]:
                continue
            for second_idx in range(first_idx+1,len(nums)):
                if second_idx>first_idx+1 and nums[second_idx] == nums[second_idx-1]:
                    continue
                third_idx = second_idx+1
                fourth_idx = len(nums)-1
                while third_idx<fourth_idx:
                    s = nums[first_idx]+nums[second_idx]+nums[third_idx]+nums[fourth_idx]
                    if s < target:
                        third_idx+=1
                    elif s > target:
                        fourth_idx-=1
                    else:
                        quadruplets.append([nums[first_idx],nums[second_idx],nums[third_idx],nums[fourth_idx]])
                        third_idx+=1
                        while third_idx < len(nums) and nums[third_idx-1]==nums[third_idx]:
                            third_idx+=1
        return quadruplets

s = Solution()
print(s.fourSum([2,2,2,2,2],8))
