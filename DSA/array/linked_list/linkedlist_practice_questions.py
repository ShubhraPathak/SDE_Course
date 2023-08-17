# Definition for singly - linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_length(head):
    if head is None:
        return
    count = 0
    itr = head
    while itr:
        count += 1
        itr = itr.next
    return count


class Solution:

    def insert_at_end(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = ListNode(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        return self.head

    # Solution 1: run time 32ms, space 16.11mb beats 97% people
    def removeNthFromEnd_Solution1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # as nth node from end is given, lets calculate the length of the ll
        length = get_length(head)

        index_to_remove = length - n

        if index_to_remove == 0:
            head = head.next
            return head

        itr_count = 0
        itr = head
        while itr:
            if itr_count == index_to_remove - 1:
                itr.next = itr.next.next
                break
            itr_count += 1
            itr = itr.next
        return head

    # Solution 2: 2 pointer solution
    def removeNthFromEnd_solution2(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        print('currenct fast and slow pointer:', fast.val, slow.val)
        for _ in range(n):
            print('printing n and fast val: ', _, fast.val)
            fast = fast.next
        print(fast.val)
        if not fast:
            return head.next
        while fast.next:
            print('in while fast.next value:', fast.next.val)
            print('in while loop fast and slow value', fast.next.val, slow.next.val)
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        itr = head
        while itr and itr.next:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next
        return head

if __name__ == '__main__':
    object_of_ll = Solution()
    array = object_of_ll.insert_values(["banana", "mango", "grapes", "orange", "figg", 'chiku', 'piku'])
    object_of_ll.removeNthFromEnd_solution2(array, 4)


