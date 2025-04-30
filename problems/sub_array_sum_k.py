'''
The intuition behind this problem is the property of prefix sum array

A prefix sum array is an array where pref_sum_arr[i] = sum of all elements from 0 to i
Sum of any sub array of our array which starts with i ends with j (including j) can be represented
as pref_sum_arr[j] - pref_sum_arr[i-1]

We need to find total number of sub arrays that add upto k, let say any sub array defined by i,j adds upto k.
we can say 
pref_sum_arr[j] - pref_sum_arr[i-1] - k
pref_sum_arr[j] - k = pref_sum_arr[i-1]

This implies if j is the end of a valid sub array pref_sum_arr[j] - k will be an element in the pref_sum_arr at starting
idx of valid sub array. GODDAMN GENIUS, HOW AM I SUPPOSED TO FIGURE THIS OUT IN AN INTERVIEW?!
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        sum_count = {0:1}
        ans = 0
        for num in nums:
            sum+=num
            if sum-k in sum_count:
                ans+=sum_count[sum-k]
            if sum not in sum_count:
                sum_count[sum] = 0
            sum_count[sum]+=1
        return ans


s = Solution()
print(s.subarraySum([1,-1,0], 0))
