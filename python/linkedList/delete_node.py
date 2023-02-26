
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

    def delete(self, target):
        # node = self.head
        # head = node
        # while (node and node.next):
        #     while node.next.data == target:
        #         node.next = node.next.next
        #         node = node.next
        #     return head.next if head.data == target else head

        head = self.head

        while head is not None and head.data == target:
            nodeToDelete = head
            head = head.next
            print(nodeToDelete.data, head)
            del nodeToDelete
            

        # 2. create a temp node to traverse through the
        # list and delete nodes with value equal to
        # target and adjust links accordingly
        temp = head
        if temp is not None:
            while temp.next is not None:
                # print()
                if temp.next.data == target:
                    nodeToDelete = temp.next
                    temp.next = temp.next.next
                    del nodeToDelete
                else:
                    temp = temp.next

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=' ->')
            current = current.next
        print("\n")


ll = LinkedList()
s = [12, 12, 12, 12]
# s = [12, 10, 12, 15, 12, 13, 20, 12, 14]
for item in s:
    ll.push(item)

print('list before deleting nodes 12')
ll.printList()
ll.delete(12)
print('list after deleting nodes 12')
ll.printList()
