class Solution:
    def findMin(self, nums):
        '''
        The intuition of this problem seems very easy but you can easily run into a lot of annoying edge cases.

        Initialize left and right pointers to 2 ends of the array. 
        - Check if the nums[l:r+1] is sorted by checking nums[l] < nums[r]. This means the smallest element of this
          sorted sub array might be our one of our candidates
        - If it is not sorted then find the mid point between the 2 and check if l to mid is sorted. If so then the pivot
          is in the right section, so we will update l to mid+1. One edge case to take not here is since we are doing
          (l+r)//2 for mid, there is a chance l and m are the same idx so need to check for nums[l] <= nums[mid] case
        - If this subarray is not sorted then the pivot is inside here which means we need to focus on this side by
          setting r = mid-1
        - There is another edge case where the min element landed at the middle. In this case both left side and right
          side will be sorted. Hence we will consider each mid point as a potential mid point candidate
        '''
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(res,nums[mid])

            if nums[l] <= nums[mid]:
                l=mid+1
            else:
                r = mid-1

        return res

s = Solution()
print(s.findMin([2,3,4,5,1]))
         