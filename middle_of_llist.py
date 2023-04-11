from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode(1) # declaring data in each node
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b # link first node to second node
b.next = c
c.next = d

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        l = 0
        while head:
            l += 1
            head = head.next

        mid = l // 2
        while mid:
            res = res.next
            mid -= 1
        print(res.val)
        return res


        # def reverse(curr=head, val=0):
        #     if curr:
        #         for i in reverse(curr.next, val+1):
        #             yield i
        #         yield [curr, val]
        # def forward(curr=head, val=0):
        #     if curr:
        #         yield [curr, val]
        #         for i in forward(curr.next, val+1):
        #             yield i
        # def middle():
        #     front = forward()
        #     end = reverse()
        #     for left, right in zip(front, end):
        #         if left[1] >= right[1]:
        #             return left[0]
        # return middle()

# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         def llist(head, target=None):
#             lst = []
#             while True:
#                 nxt = head.next
#                 lst.append(head.val)
#                 if nxt:
#                     head = nxt
#                     if target == head.val:
#                         return head
#                 else:
#                     return lst
#
#         lst = llist(head)
#         if len(lst) == 1:
#             return llist(head, lst[0])
#         mid_el = lst[int(len(lst) / 2)]
#
#         return llist(head, mid_el)



obj = Solution()
print(obj.middleNode(a))