/**
 * @url - https://dev.to/theabbie/swap-nodes-in-pairs-gng
 * 
 * Given a linked list, swap every two adjacent nodes and return its head. 
 * You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
 * 
 *  @constraint 0 >= nums.length <= 100
 * 
 * @param nums array
 * @returns the swapped pairs list
 */

function SwapAdjacent(nums: number[]) {
    if (nums.length < 0 && nums.length > 100) return;
    if (nums.length === 1) return nums;

    const result: number[] = [];

    for (let index = 0; index < nums.length; index += 2) {
        const element = nums[index];
        const elementNext = nums[index + 1];

        result.push(elementNext, element);
    }

    return result;
}

console.log('SwapAdjacent: ', SwapAdjacent([1, 2, 3, 4]));
console.log('SwapAdjacent: ', SwapAdjacent([]));
console.log('SwapAdjacent: ', SwapAdjacent([1]));
console.log('SwapAdjacent: ', SwapAdjacent([1, 2]));
