
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

    def swap(self, a, b):
        if a == b:
            return
        current = self.head

        nodeA = None
        nodeB = None

        while current.next != None:
            if current.next.data == a:
                nodeA = current
            if current.next.data == b:
                nodeB = current

            if nodeA != None and nodeB != None:
                break

            current = current.next

        if (nodeA != None and nodeB != None):
            self.swapNodes(nodeA, nodeB)

    def swapNodes(self, nodeA, nodeB):
        temp = nodeA.next
        nodeA.next = nodeB.next
        nodeB.next = temp

        temp = nodeA.next.next
        nodeA.next.next = nodeB.next.next
        nodeB.next.next = temp

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("\n")


ll = LinkedList()
s = [10, 15, 12, 13, 20, 14]
for item in s:
    ll.push(item)

print('list before swapping nodes')
ll.printList()
ll.swap(12, 20)
print('list after swapping nodes')
ll.printList()
