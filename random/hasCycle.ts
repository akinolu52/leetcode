/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function hasCycle(head: ListNode | null): boolean {
    /**
        - the idea is to transverse the linked-list
        - then check if the the nodes already exist
        - if it does return true
        - if it does not add it to the set
    */
    const s = new Set();
    let current: ListNode = head;

    while (current) {
        if (s.has(current)) return true;

        s.add(current);
        current = current.next;
    }

    return false
};