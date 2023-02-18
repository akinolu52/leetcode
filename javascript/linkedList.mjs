
let head;

class Node {
    constructor(value) {
        this.data = value;
        this.next = null;
    }
}

function printList() {
    let temp = head

    while (temp !== null) {
        console.log(temp.data)
        temp = temp.next
    }
}


head = new Node(1);
const second = new Node(2);
const third = new Node(3);

head.next = second;
second.next = third;

printList()

// module.export = { Node, printList };
export { Node, printList };
