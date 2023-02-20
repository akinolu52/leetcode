
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

    def isPalindrome(self) -> bool:
        stack = []
        current = self.head

        # push data into stack
        while current:
            stack.append(current.data)
            current = current.next
        
        current = self.head
        while current:
            if current.data != stack.pop():
                return False
            
            current = current.next

        return True

    def printList(self):
        current = self.head

        while current:
            print(current.data, end=' -> ')
            current = current.next

    def clear(self) -> None:
        self.head = None


ll = LinkedList()
s = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
for item in s:
    ll.push(item)

print("isPalindrome:", ll.isPalindrome())

ll.clear()

s = [1, 2, 3, 4, 3, 2, 1]
for item in s:
    ll.push(item)
print("isPalindrome:", ll.isPalindrome())

ll.clear()

s = [1, 0, 0]
for item in s:
    ll.push(item)
print("isPalindrome:", ll.isPalindrome())
