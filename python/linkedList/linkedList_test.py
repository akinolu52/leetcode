from linkedList import LinkedList, Node

lList = LinkedList()

lList.head = Node(1)
second = Node(2)
third = Node(3)

lList.head.next = second
second.next = third

lList.printList()

