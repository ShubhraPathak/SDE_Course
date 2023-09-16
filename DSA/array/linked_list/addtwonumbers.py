# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# 2->8->3 and 5->2->4 = 7->0->8
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddNumbers:

    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linked_list_string = ''
        while itr:
            linked_list_string += str(itr.val) + '--->'
            itr = itr.next

        print(linked_list_string)

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        self.head = ListNode()
        output = self.head
        while l1 is not None or l2 is not None or carry != 0:
            x = l1.val if l1 else None
            y = l2.val if l2 else None
            total = x+y+carry
            carry = total//10
            remainder = total % 10
            new_node = ListNode(remainder)
            output.next = new_node
            output = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return self.head.next


if __name__ == '__main__':
    ll = AddNumbers()
    ll.head = ListNode(1)
    first = ListNode(2)
    second = ListNode(8)
    l_1 = ll.head
    l_1.next = first
    first.next = second
    ll.head = ListNode(2)
    first_2 = ListNode(8)
    second_2 = ListNode(0)
    l_2 = ll.head
    l_2.next = first_2
    first_2.next = second_2
    ll.add_two_numbers(l_1, l_2)
    ll.printll()

