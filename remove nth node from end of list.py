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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        trav = head
        size = 0
        while True:
            size += 1
            trav = trav.next
            if trav == None:
                break

        if size == 1:
            return None

        if size == n:
            return head.next

        trav = head
        while size != n + 1:  # or you can write size - n - 1 != 0 :
            trav = trav.next
            n += 1

        trav.next = trav.next.next
        return head

        # result = head
        # before = head
        # after = head
        #
        # llist_len = 0
        # while head:
        #     llist_len += 1
        #     head = head.next
        #
        # before_count = 1
        # element_before = llist_len - n
        # while before_count < element_before:
        #     before = before.next
        #     before_count += 1
        #
        # after_count = 0
        # element_after = llist_len - n + 1
        # while after_count < element_after:
        #     after = after.next
        #     after_count += 1
        #
        # # before.next = after
        #
        # while result:
        #     if result == before:
        #         result.next = after
        #         return result
        #     else:
        #         result = result.next



obj = Solution()
b = obj.removeNthFromEnd(a, 2)
print(b.val)
