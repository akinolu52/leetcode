/**
 * @url -  https://dev.to/theabbie/remove-one-element-to-make-the-array-strictly-increasing-hki
 * 
 * Given a 0-indexed integer array nums,
 * return true if it can be made strictly increasing after removing exactly one element, or false otherwise.
 * If the array is already strictly increasing, return true.
 * 
 * @constraint 2 <= nums.length <= 1000
 * 
 * @param nums: a list of numbers
 * @returns a boolean value indicating if it can be sorted by removing a single value
 */

function canBeIncreasing(nums: number[]) {
  if (nums.length < 2 || nums.length > 1000) return false;
  if (new Set(nums).size === 1) return false;
  if (nums.join("") === [...nums].sort((a, b) => a - b).join("")) return true;

  for (let index = 0; index < nums.length; index++) {
    const numbers = [...nums];

    numbers.splice(index, 1);

    let numbersSort = [...numbers].sort((a, b) => a - b);
    if (numbers.join("") === numbersSort.join("")) return true;
  }

  return false;
}

console.log("canBeIncreasing: ", canBeIncreasing([1, 1, 1]));
console.log("canBeIncreasing: ", canBeIncreasing([1, 2, 3]));
console.log("canBeIncreasing: ", canBeIncreasing([2, 3, 1, 2]));
console.log("canBeIncreasing: ", canBeIncreasing([1, 2, 10, 5, 7]));
