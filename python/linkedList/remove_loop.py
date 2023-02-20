
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def detectAndRemoveLoop(self) -> bool:
        s = set()
        current = self.head

        while current:
            if current.next in s:
                current.next = None

            s.add(current)
            current = current.next

        return False

    def printList(self):
        current = self.head

        while current:
            # print('here ', current.data)
            print(current.data, end=' -> ')
            current = current.next


ll = LinkedList()
ll.push(10)
ll.push(4)
ll.push(15)
ll.push(20)
ll.push(50)

ll.head.next.next.next.next.next = ll.head.next.next
print("Linked List before removing loop")
# ll.printList()

ll.detectAndRemoveLoop()

print("Linked List after removing loop")
ll.printList()


# 50 -> 20 -> 15 -> 4 -> 10 => 15
