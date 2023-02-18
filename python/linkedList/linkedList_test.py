from linkedList import LinkedList, Node

lList = LinkedList()

lList.head = Node(1)
second = Node(2)
third = Node(3)

lList.head.next = second
second.next = third

lList.printList()

lList.append(6)

lList.push(7)

lList.push(1)

lList.append(4)

lList.insertAfter(lList.head.next, 8)

lList.printList()
