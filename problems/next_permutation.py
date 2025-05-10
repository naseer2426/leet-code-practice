'''
The intuition behind this problem is to consider the array digits of a number. Our task is to find the closest next number
we can create using the same digits

If we swap numbers towards the right of the number, the change will be least, the least change we can make to this number
is swapping the last and second last number

So first step to solve this problem is find the min indx of modification. The swaps will be fixed to indices afte this index.

We iterate backwards from the end and find the first index which is lower then its next element. This implies something bigger
from the right can swap it to make a bigger number.

If this index does not existing the array is sorted in desc order, we simply return the sorted order instead

Once we find this min index, then we find the lowest number from index > this min index which is larger than the min index value.
This value is swapped with the min index of modification

From the logic we have followed above we can conclude that the sub array min_idx_of_mod+1:len(nums) is sorted in desc order now.
Otherwise we would have found a larger idx where nums[idx] < nums[idx+1]. The swap will not change the sorted desc nature of this sub array

So as a final step we sort this sub array to find the smallest number

oof.
'''

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        min_idx_of_mod = l-2
        while min_idx_of_mod >= 0:
            if nums[min_idx_of_mod] < nums[min_idx_of_mod+1]:
                break
            min_idx_of_mod-=1
        if min_idx_of_mod == -1:
            nums.sort()
            return

        for i in range(l-1,min_idx_of_mod,-1):
            if nums[i] > nums[min_idx_of_mod]:
                break
        nums[min_idx_of_mod], nums[i] = nums[i], nums[min_idx_of_mod]
        self.reverse(nums,min_idx_of_mod+1,l-1)
        
    def reverse(self,nums,i,j):
        left = i
        right = j
        while left < right:
            nums[left],nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        


s = Solution()
a = [2,3,1]

s.nextPermutation(a)
print(a)

