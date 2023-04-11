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

a1 = ListNode(11)  # declaring data in each node
b1 = ListNode(22)
c1 = ListNode(44)
a2 = ListNode(11)
b2 = ListNode(33)
c2 = ListNode(44)

a1.next = b1
b1.next = c1

a2.next = b2
b2.next = c2

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head

        l = 0
        while current_node:
            current_node = current_node.next
            l += 1

        middle_of_llist = l // 2
        current_node = head

        while middle_of_llist > 0:
            middle_of_llist -= 1
            current_node = current_node.next

        return current_node

    def removeNthFromStart(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head

        # Найдем элементы до и после искомого
        # Найдем для начала искомый
        l = 0
        while l != n:
            current_node = current_node.next
            l += 1

        # Определим следующий элемент
        right_node = current_node.next

        # Определим предыдущий элемент
        left_node = head
        while left_node.next != current_node:
            left_node = left_node.next

        left_node.next = right_node
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head

        # Найдем элементы до и после искомого
        # Найдем для начала искомый
        l = 0
        while current_node:
            current_node = current_node.next
            l += 1

        target_node = l - n
        target_counter = 0
        current_node = head

        while target_counter != target_node:
            current_node = current_node.next
            target_counter += 1

        # Определим следующий элемент
        right_node = current_node.next

        # Определим предыдущий элемент
        left_node = head
        if left_node == current_node:
            left_node = left_node.next
            return left_node

        while left_node.next != current_node:
            left_node = left_node.next

        left_node.next = right_node
        return head

    def add_to_end(self, head):
        current_node = head
        while current_node.next:
            current_node = current_node.next
        current_node.next = ListNode(66)
        tail = current_node.next
        return tail.val

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        current = dummy = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2, current = list2.next, list2
            else:
                current.next = list1
                list1, current = list1.next, list1
        if list1 or list2:
            current.next = list1 if list1 else list2
        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev



obj = Solution()
print(obj.reverseList(a))
#print(obj.mergeTwoLists(a1, a2))
#print(obj.add_to_end(a))
#print(obj.removeNthFromStart(a, 1))
#print(obj.middleNode(a))
