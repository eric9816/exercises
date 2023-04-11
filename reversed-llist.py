from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(11) # declaring data in each node
b = ListNode(22)
c = ListNode(33)
d = ListNode(44)
e = ListNode(55)

a.next = b # link first node to second node
b.next = c
c.next = d
d.next = e

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

        # node_lst = []
        # while head:
        #     node_lst.append(head)
        #     head = head.next
        #
        # reversed_lst = list(reversed(node_lst))
        # for idx, node in enumerate(reversed_lst):
        #     if idx < len(reversed_lst) - 1:
        #         node.next = reversed_lst[idx+1]
        # return node




obj = Solution()
obj.reverseList(a)