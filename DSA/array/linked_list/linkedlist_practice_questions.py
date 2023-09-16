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
        print('current fast and slow pointer:', fast.val, slow.val)
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

    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        itr = head
        while itr and itr.next:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next
        return head

    # Find middle element

    def find_middle_elem_solution1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        length = get_length(head)
        middle = length//2
        itr = head
        count = 0
        while itr:
            if count == middle:
                print("element at middle is: ", itr.val)
                return itr.val
            count += 1
            itr = itr.next

    def find_middle_2_pointers(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow_pt = head
        fast_pt = head
        while fast_pt and fast_pt.next:
            slow_pt = slow_pt.next
            fast_pt = fast_pt.next.next
        print("middle value from 2 pointer solution is:", slow_pt.val)
        return slow_pt


    def check_if_linked_list_circular(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            print("Head is null meaning empty linked list, it is a circular linked list")
            return True

        node = head.next

        while node and node != head:
            node = node.next

        return (node == head)

    # count nodes in circular linked list
    def count_nodes_in_circular_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next
        count = 1  # start point is node.next hence starting the count from 1
        while node and node != head:
            node = node.next
            count += 1
            if node == head:
                break
        print("total nodes in circular linked list is:", count)
        return count

        # temp = head
        # result = 0
        # if (head != None):
        #     while True:
        #         temp = temp.next
        #         result = result + 1
        #         if (temp == head):
        #             break
        # print("total nodes in circular linked list is:", result)
        # return result

    def exchange_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Given linked list is a circular one. Iterate until node.next is not head.
        node = head
        while node.next != head:
            node = node.next  # this will be tail of linked list
        temp = head.val
        node.val = head.val
        head.val = temp
        return head



if __name__ == '__main__':
    object_of_ll = Solution()
    array = object_of_ll.insert_values(["banana", "mango", "grapes", "orange", "figg", 'chiku', 'piku'])
    object_of_ll.removeNthFromEnd_solution2(array, 4)
    int_array = object_of_ll.insert_values([2,1,2,3,232,455,646,32,12,12,29,24])
    object_of_ll.find_middle_elem_solution1(int_array)
    object_of_ll.find_middle_2_pointers(int_array)
    object_of_ll.head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    object_of_ll.head.next = second
    second.next = third
    third.next = fourth
    if object_of_ll.check_if_linked_list_circular(object_of_ll.head):
        print("TRUE")
    else:
        print("FALSE")
    fourth.next = object_of_ll.head
    # print("List before exchange")
    # object_of_ll.printll()

    if object_of_ll.check_if_linked_list_circular(object_of_ll.head):
        print("TRUE")
    else:
        print("FALSE")

    print("list after exchange")
    object_of_ll.exchange_nodes(object_of_ll.head)
    # object_of_ll.printll()
    object_of_ll.count_nodes_in_circular_linked_list(object_of_ll.head)


