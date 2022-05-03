/**
 * A solution to the count the number of 1s in a binary number.
 * URL: https://leetcode.com/problems/number-of-1-bits/
 * /


/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
    const count = (n.toString(2).match(/1/g) || []).length

    return count;
};

var hammingWeight2 = function (n) {
    const count = n.toString(2).split(/1/g).length - 1;
    console.log(count);

    return count;
};