'''
 - traverse through the linked-list
 - check if the current node is in the set
 - while traversing we save each node into a set
 - if it's return true
 - else return false
'''

def hasCycle(self, head: Optional[ListNode]) -> bool:
    s = set()
    current = head

    while current:
        if current in s:
            return True

        s.add(current)
        current = current.next

    return False
