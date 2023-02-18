from linkedList import LinkedList, Node

lList = LinkedList()

lList.head = Node(1)
second = Node(2)
third = Node(3)

lList.head.next = second
second.next = third

lList.printList()

lList.insertAtTail(6)

lList.insertAtHead(7)

lList.insertAtHead(1)

lList.insertAtTail(4)

lList.insertAfter(lList.head.next, 8)

lList.printList()
