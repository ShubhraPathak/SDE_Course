class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def printll(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linked_list_string = ''
        while itr:
            linked_list_string += str(itr.data) + '--->'
            itr = itr.next

        print(linked_list_string)

    def get_length(self):
        if self.head is None:
            raise Exception("Head is none, list empty")

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        # current head will be next node now hence, Node(data, next) is having Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if self.head is None:
            raise Exception("Empty list")
        if index < 0 or index >= self.get_length():
            raise Exception("List index out of range")

        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:  # In linked list insertion we always change the reference of previous node.
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if self.head is None:
            raise Exception("Empty list")
        if index < 0 or index >= self.get_length():
            raise Exception("List index out of range")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        return self.head

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data_to_remove):
        if self.head is None:
            return

        if self.head.data == data_to_remove:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.next.data == data_to_remove:
                itr.next = itr.next.next
                break
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(8)
    ll.printll()
    ll.insert_at_beginning(90)
    ll.printll()
    ll.insert_at_beginning(81)
    ll.printll()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.printll()
    ll.insert_at(1, "ROSS")
    ll.printll()
    ll.insert_at_end("FIGGGGSSSS")
    ll.printll()
    ll.insert_after_value("mango", "Apple")
    ll.printll()
    ll.remove_by_value("FIGGGGSSSS")
    ll.printll()
