# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head == None:
            return None
        size = 0
        curr = head
        while curr!=None:
            size +=1
            curr = curr.next

        target = size - n + 1

        prev = None
        curr = head
        curr_node_num = 1

        while curr != None:
            
            if curr_node_num == target and prev == None:
                return curr.next
            if curr_node_num == target:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            curr_node_num +=1

        return head

def conv_list_to_nodes(l):
    if len(l) == 0:
        return None
    head = ListNode(val=l[0])
    curr = head
    for i in range(1,len(l)):
        next = ListNode(val=l[i])
        curr.next = next
        curr = next
    return head

def conv_nodes_to_list(head):
    if head == None:
        return []
    curr = head
    l = []
    while curr != None:
        l.append(curr.val)
        curr = curr.next
    return l

s = Solution()
print(conv_nodes_to_list(s.removeNthFromEnd(conv_list_to_nodes([1,2,3,4,5]),5)))
