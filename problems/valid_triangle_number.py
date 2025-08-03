class Solution:
    def triangleNumber(self, nums):
        '''
        When I first read this problem I thought of it as, given any 2 a & b, a third number c will be a valid triangle number if
            - a+b>c
            - abs(a-b)<c
        My idea was if I can somehow validate these 2 conditions in o(1) time then I can get a N^2 solution but I was not able to find one

        The correct solution is to use c as the starting point and find all possible a & b. By sorting the array and assuming all a & b we 
        will find will be before c in the sorted order, condition 2 is automatically guaranteed

        For condition 1, we can initialize 2 pointers at the start and end of sub array before c and find the sums that are > c
        '''
        nums.sort()
        N = len(nums)
        ans = 0
        for k in range(2,N):
            i,j = 0,k-1
            while i<j:
                if nums[i]+nums[j] > nums[k]:
                    ans+=j-i
                    j-=1
                else:
                    i+=1
        return ans

s = Solution()
print(s.triangleNumber([2,2,2,2]))
