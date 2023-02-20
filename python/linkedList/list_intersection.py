
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

    def intersect(self, l1, l2) -> Node:
        current = l1.head
        s = {current.data}
        res = None

        while current:
            s.add(current.data)
            current = current.next
            if current is None:
                break

        current = l2.head
        res = []
        while current:
            if current.data in s:
                res.append(current.data)
            current = current.next

        result = LinkedList()

        for item in sorted(res, reverse=True):
            result.push(item)

        return result

    def printList(self, node):
        current = node.head

        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("\n")


ll = LinkedList()
ll2 = LinkedList()

s = [2, 3, 4]
for item in s:
    ll.push(item)

s = [5, 4, 3, 2, 1]
for item in s:
    ll2.push(item)

res = ll.intersect(ll, ll2)
ll.printList(res)
