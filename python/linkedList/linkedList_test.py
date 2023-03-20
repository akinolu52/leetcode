from linkedList import LinkedList, Node

ll = LinkedList()

ll.head = Node(1)
second = Node(2)
third = Node(3)

ll.head.next = second
second.next = third

ll.printList()

# ll.insertAtTail(6)

# ll.insertAtHead(7)

# ll.insertAtHead(1)

# ll.insertAtTail(4)

# ll.insertAfter(ll.head.next, 8)

# ll.printList()

# const x = undefined;

# if (x) {
#      console.log('okay')
# }


# head -> 1 (next -> 2 -> next -> 3)
# 1 -> 2 -> 3 -> %  

# temp = head

# while temp:
#     print(temp.data)
#     temp = temp.next





