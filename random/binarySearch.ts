/**
 * best suited for sorted array => log n
 * @param sortedArr sorted array
 * @param find number to find
 * @returns index
 */

function binarySearch(sortedArr: Array<string | number>, find: string | number): number {
    let left = 0;
    let right = sortedArr.length - 1;

    let count = 0;
    while (left <= right) {
        console.log('run ', ++count)
        const mid = Math.floor((left + right) / 2);
        const midValue = sortedArr[mid];

        if (find === midValue) return mid;
        else if (find < midValue) right = mid - 1;
        else left = mid + 1;
    }

    // console.log(mp);
    
    return -1;
};


let arr = [10, 20, 30, 35, 40];
let find = 35

console.log(binarySearch(arr, find))