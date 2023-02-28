
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

    def reverse(self) -> Node:
        previous = None
        current = self.head

        while current:
            temp = current.next

            current.next = previous
            previous = current

            current = temp


    def printList(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("\n")


ll = LinkedList()
ll2 = LinkedList()

s = [8, 7, 6, 5, 4, 3, 2, 1]
for item in s:
    ll.push(item)

print('linked list before reversal')
ll.printList()
ll.reverse()
print('linked list after reversal')
ll.printList()

# s = [5, 4, 3, 2, 1]
# for item in s:
#     ll2.push(item)


# print('linked list before reversal')
# ll2.printList()
# ll2.reverse()
# print('linked list after reversal')
# ll2.printList()
