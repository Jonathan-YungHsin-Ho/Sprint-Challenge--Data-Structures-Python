from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # self.current stores the current oldest element
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif len(self.storage) == self.capacity:
            self.current.insert_before(item)
            self.storage.length += 1

            if self.current == self.storage.head:
                self.storage.move_to_front(self.current.prev)

            if self.current == self.storage.tail:
                self.current = self.storage.head
                self.storage.delete(self.storage.tail)
            else:
                self.current = self.current.next
                self.storage.delete(self.current.prev)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
