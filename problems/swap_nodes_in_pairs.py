# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        
        curr_idx = -1
        prev = None
        dummy_node = ListNode()
        dummy_node.next = head
        curr = dummy_node
        while curr != None:
            # print(f"curr - {curr.val}, prev - {prev.val if prev!=None else None}, next - {curr.next.val if curr.next != None else None}")
            if curr_idx%2!=0:
                prev = curr
                curr = curr.next
                curr_idx+=1
                continue
            # print("swap started")
            next = curr.next
            if next != None:
                curr.next = next.next
                next.next = curr
                prev.next = next
            prev = next
            curr_idx+=1
        return dummy_node.next


def run_test_case(lst):
    head = ListNode(val=lst[0])
    curr = head
    for i in range(1,len(lst)):
        curr.next = ListNode(val=lst[i])
        curr = curr.next
    s = Solution()
    new_head = s.swapPairs(head)
    new_lst = []
    curr = new_head
    while curr!=None:
        new_lst.append(curr.val)
        curr = curr.next
    print(new_lst)

run_test_case([1,2,3])
