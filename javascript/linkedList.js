class Node {
    constructor(data, next = null) {
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.size = 0;
    }

    checkIfOutOfBounds(index) {
        if (index < 0 || index > this.size) {
            return true;
        }
        return false;
    }

    // insert first node
    insertFirstNode(data) {
        this.head = new Node(data, this.head);
        this.size++;
        return;
    }

    // insert last node
    insertLastNode(data) {
        let node = new Node(data);
        let current = this.head;

        // if there's no item in the linked list
        if (this.size === 0) {
            this.head = node
            this.size++;

            return;
        }

        // get to the last node with data
        while (current.next) {
            current = current.next;
        }

        current.next = node;
        this.size++;
        return;
    }

    // insert at index
    insertAtIndex(data, index) {
        if (this.checkIfOutOfBounds(index)) {
            return;
        }

        const node = new Node(data);
        let current = this.head;
        let previous = null;
        let count = 0;

        // insert at the first
        if (index === 0) {
            this.head = node;
            return;
        }

        // get previous and current
        while (count < index) {
            previous = current;
            current = current.next;
            count++;
        }

        previous.next = node;
        node.next = current.next;

        return;
    }

    // get at index
    getAtIndex(index) {
        if (this.checkIfOutOfBounds(index)) {
            return;
        }

        if (index === 0) {
            console.log(`value at index ${index} => `, this.head.data);
            return;
        }

        let count = 1;
        let current = this.head.next;

        while (current) {
            if (count == index) {
                console.log(`value at index ${index} => `, current.data);
                return;
            }

            current = current.next;
            count++;
        }
    }

    // remove at index
    removeAtIndex(index) {
        if (this.checkIfOutOfBounds(index)) {
            return;
        }

        if (this.head == null) return;

        let current = this.head;
        let count = 0;
        let previous = null

        if (index === 0) {
            this.head = current.next;
        } else {

            while (count < index) {
                previous = current;
                current = current.next;
                count++;
            }

            previous.next = current.next
        }

        this.size--;
        console.log(`removed item at index ${index} => `, current.data);
        return;
    }

    // remove value
    removeValue(value) {
        // if (this.checkIfOutOfBounds(index)) {
        //     return;
        // }

        if (this.head == null) return;

        let current = this.head;
        let count = 0;
        let previous = null

        if (current.data === value) {
            this.head = current.next;
        }

        while (current.next) {
            if (current.data === value) {
                current.value = current.next.value
                current.next = current.next.next
            }

            current = current.next
            this.printList();
        }
    }
    // clear list
    clearList() {
        this.size = 0;
        this.head = null;
    }

    // print list data
    printList() {
        let current = this.head;
        const result = []

        while (current) {
            result.push(current.data);
            current = current.next;
        }

        console.log('\n', '(' + result.join(') -> (') + ')', '\n');
        return;
    }

}


const ll = new LinkedList();

ll.insertFirstNode(300)
ll.insertFirstNode(200)
ll.insertFirstNode(100)
// ll.insertFirstNode(300)
// ll.insertFirstNode(300)
// ll.insertFirstNode(300)
// ll.insertLastNode(500)
ll.insertLastNode(300)

ll.printList()

// ll.insertAtIndex(400, 2)
// ll.getAtIndex(0)
// ll.getAtIndex(3)

// ll.printList()

ll.removeValue(300)
// ll.removeAtIndex(0)

// ll.printList()

// ll.removeAtIndex(2)

// ll.printList()

// ll.clearList()

ll.printList()

// console.log(ll)