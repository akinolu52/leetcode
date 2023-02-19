
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

    def detectLoop(self) -> bool:
        s = set()
        current = self.head

        while current:
            if current in s:
                return True

            s.add(current)
            current = current.next

        return False


# Driver program for testing
ll = LinkedList()
ll.push(20)
ll.push(4)
ll.push(15)
ll.push(10)

# Create a loop for testing
ll.head.next.next.next.next = ll.head

if (ll.detectLoop()):
    print("Loop Found")
else:
    print("No Loop ")
