from itertools import combinations
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # scuffed solution, I have no idea whats going on but it works
        valid_sets = []
        dedup = {}
        num_count = {}
        for i in range(len(nums)):
            if nums[i] in num_count:
                num_count[nums[i]]+=1
            else:
                num_count[nums[i]] = 1
        unique = num_count.keys()

        for set_2 in combinations(unique,2):
            third = 0 - (set_2[0]+set_2[1])
            if third not in num_count:
                continue
            num_count[set_2[0]]-=1
            num_count[set_2[1]]-=1
            num_count[third]-=1
            if num_count[third] < 0:
                num_count[set_2[0]]+=1
                num_count[set_2[1]]+=1
                num_count[third]+=1
                continue
            sorted_set = sorted([ set_2[0],set_2[1],third])
            set_key = str(sorted_set[0])+str(sorted_set[1])+str(sorted_set[2])
            if set_key in dedup:
                num_count[set_2[0]]+=1
                num_count[set_2[1]]+=1
                num_count[third]+=1
                continue
            num_count[set_2[0]]+=1
            num_count[set_2[1]]+=1
            num_count[third]+=1
            dedup[set_key] = True
            valid_sets.append(sorted_set)
        for num in unique:
            if num_count[num] < 2:
                continue
            set_2 = [num,num]
            third = 0 - (set_2[0]+set_2[1])
            if third not in num_count:
                continue
            num_count[set_2[0]]-=1
            num_count[set_2[1]]-=1
            num_count[third]-=1
            if num_count[third] < 0:
                num_count[set_2[0]]+=1
                num_count[set_2[1]]+=1
                num_count[third]+=1
                continue
            sorted_set = sorted([ set_2[0],set_2[1],third])
            set_key = str(sorted_set[0])+str(sorted_set[1])+str(sorted_set[2])
            if set_key in dedup:
                num_count[set_2[0]]+=1
                num_count[set_2[1]]+=1
                num_count[third]+=1
                continue
            num_count[set_2[0]]+=1
            num_count[set_2[1]]+=1
            num_count[third]+=1
            dedup[set_key] = True
            valid_sets.append(sorted_set)
        
        for num in unique:
            if num_count[num] < 3:
                continue
            if num+num+num == 0 and not dedup[str(num)+str(num)+str(num)]:
                valid_sets = [num,num,num]
        return valid_sets



s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
