/**
 * A solution to the count the longest substring with k unique characters.
 * URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * /

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    const result = new Map();
    let count = 0;

    for (let i = 0; i < s.length; i++) {
        const current = s.charAt(i);
        if (result.has(current)) {
            i = result.get(current);
            result.clear();
        } else {
            result.set(current, i);
        }

        if (result.size > count) {
            count = result.size;
        }
    }

    return count;
};
