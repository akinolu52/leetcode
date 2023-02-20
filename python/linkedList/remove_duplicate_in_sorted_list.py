
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

    def removeDuplicate(self):
        current = self.head

        while current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("\n")

    def clear(self) -> None:
        self.head = None


ll = LinkedList()
s = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
s.sort(reverse=True)
for item in s:
    ll.push(item)

print('list before duplicate removal')
ll.printList()
ll.removeDuplicate()
print('list after duplicate removal')
ll.printList()


ll.clear()


s = [1, 2, 3, 4, 3, 2, 1]
s.sort(reverse=True)
for item in s:
    ll.push(item)

print('list before duplicate removal')
ll.printList()
ll.removeDuplicate()
print('list after duplicate removal')
ll.printList()


ll.clear()

s = [1, 0, 0]
s.sort(reverse=True)
for item in s:
    # print(s, item)
    ll.push(item)
print('list before duplicate removal')
ll.printList()
ll.removeDuplicate()
print('\nlist after duplicate removal')
ll.printList()
