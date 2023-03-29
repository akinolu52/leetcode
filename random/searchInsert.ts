function searchInsert(nums: number[], target: number): number {
    // get the position of the target in the nums and return if it's found
    const position = nums.indexOf(target);

    if (position !== -1) return position

    // if it does not exist add it to the list and return the index
    nums.push(target)
    nums.sort((a, b) => a - b)

    return nums.indexOf(target)
};