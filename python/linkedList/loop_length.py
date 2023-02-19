class Node:

    # Function to make a node
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:

    # Function to initialize the
    # head of the linked list
    def __init__(self):
        self.head = None

    # Function to insert a new
    # node at the end
    def addNode(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = Node(val)

    def createLoop(self, n):

        # LoopNode is the connecting node to
        # the last node of linked list
        LoopNode = self.head
        for _ in range(1, n):
            LoopNode = LoopNode.next

        # end is the last node of the Linked List
        end = self.head
        while (end.next):
            end = end.next

        # Creating the loop
        end.next = LoopNode

    def detectLoop(self) -> int:
        count = 0
        s = set()
        endNode = None
        current = self.head

        while current:
            if current in s:
                # there's a loop
                endNode = current
                break

            s.add(current)
            current = current.next

        if endNode is None:
            return None
        
        countValue = False
        
        for node in s:
            if countValue:
                count += 1
                continue
            if node.val != endNode.val:
                countValue = True
                
        return count


ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.addNode(5)

ll.createLoop(2)

loopLength = ll.detectLoop()

print(loopLength if ll.head is not None else "Linked list is empty")
