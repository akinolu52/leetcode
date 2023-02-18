class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # push node to the front of the list
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # insert node after a specific node
    def insertAfter(self, previousNode, data):
        if previousNode is None:
            print('Previous node must be in the LinkedList')
            return

        newNode = Node(data)
        newNode.next = previousNode.next
        previousNode.next = newNode

    # append node to the end of the linked list
    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode
