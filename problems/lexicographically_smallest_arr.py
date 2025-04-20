class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        groups = []
        curr_group = [sorted_nums[0]]
        group_idx = {sorted_nums[0]:0}
        curr_group_idx = 0  
        for i in range(1,len(sorted_nums)):
            curr_num = sorted_nums[i]
            if abs(curr_group[-1]-curr_num) <= limit:
                curr_group.append(curr_num)
                group_idx[curr_num] = curr_group_idx
            else:
                groups.append(curr_group)
                curr_group = [curr_num]
                curr_group_idx+=1
                group_idx[curr_num] = curr_group_idx
        groups.append(curr_group)
        
        smallest_lex_arr = []
        for i in nums:
            smallest_lex_arr.append(groups[group_idx[i]].pop(0))
        return smallest_lex_arr

s = Solution()
print(s.lexicographicallySmallestArray([1,5,18,9,8], 2))
