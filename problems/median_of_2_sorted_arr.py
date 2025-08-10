class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        '''
            I would never have found this solution, solved it after watching neetcode
        '''
        A,B = nums1, nums2
        if len(B) < len(A):
            A,B = B,A
        left_half_size = (len(A) + len(B))//2
        start = 0
        end = len(A)-1
        while True:
            left_a_end = (start+end)//2
            left_b_end = left_half_size - (left_a_end+1) - 1

            
            left_a_end_elem = -float("inf") if left_a_end <0 else A[left_a_end]
            left_b_end_elem = -float("inf") if left_b_end <0 else B[left_b_end]
            right_a_start_elem = float("inf") if left_a_end >= len(A)-1 else A[left_a_end+1]
            right_b_start_elem = float("inf")  if left_b_end >= len(B)-1 else B[left_b_end+1]

            #print(f"left a end idx {left_a_end}, left b idx end {left_b_end}")
            #print(f"left_a_end_elem {left_a_end_elem}, right_a_start_elem {right_a_start_elem}")
            #print(f"left_b_end_elem {left_b_end_elem}, right_b_start_elem {right_b_start_elem}")

            if left_a_end_elem <= right_b_start_elem and left_b_end_elem <= right_a_start_elem:
                if (len(A)+len(B))%2 == 0:
                    return (max(left_a_end_elem,left_b_end_elem) + min(right_a_start_elem,right_b_start_elem))/2
                else:
                    return min(right_a_start_elem,right_b_start_elem)
            if left_a_end_elem > right_b_start_elem:
                end = left_a_end-1
                continue
            if left_b_end_elem > right_a_start_elem:
                start = left_a_end+1
            #print(f"new start {start} new end {end}")
            #print("-------------------")

s = Solution()
print(s.findMedianSortedArrays([1,2,3,4,5],[6,7,8,9,10,11]))
