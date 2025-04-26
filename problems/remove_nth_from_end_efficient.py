# Definition for singly-linked list.
'''
Intuition here is that we use 2 pointers, offset the second pointer by n+1 and remove the
node after the first pointer when second hits None. This way we dont need to interate twice
'''



class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        first = head
        second = head
        count = 1

        while second != None:
            if count == n+1:
                break
            second = second.next
            count += 1

        if second == None:
            return first.next

        while first!=None:
            if second.next == None:
                first.next = first.next.next
                return head
            
            first = first.next
            second = second.next

s = Solution()
head = conv_list_to_nodes([1,2,3,4,5])
print(conv_nodes_to_list(s.removeNthFromEnd(head,5)))
