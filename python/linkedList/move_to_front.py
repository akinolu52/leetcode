
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

    def moveToFront(self):
        current = self.head
        lastNode = None

        while current.next:
            if current.next.next is None:
                lastNode = current.next.data
                current.next = None
                break
            current = current.next

        temp = self.head
        self.head = Node(lastNode)
        self.head.next = temp

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("\n")


ll = LinkedList()
# s = [10, 15, 12, 13, 20, 14]
# for item in s:
#     ll.push(item)

# print('list before replacing nodes')
# ll.printList()
# ll.moveToFront()
# print('list after replacing nodes')
# ll.printList()

s = [5, 4, 3, 2, 1]
for item in s:
    ll.push(item)

print('list before replacing nodes')
ll.printList()
ll.moveToFront()
print('list after replacing nodes')
ll.printList()
