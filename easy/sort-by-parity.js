/**
 * A solution to the Sort By Parity problem.
 * URL: https://leetcode.com/problems/sort-array-by-parit
 * /

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    const even = [];
    const odd = [];
    
    for(let i = 0; i < nums.length; i++){
        const num = nums[i];
        if(num % 2 === 0) {
            even.push(num);
        } else {
            odd.push(num);
        }
    }
    
    return [...even.sort(), ...odd];
};