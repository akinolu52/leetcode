
/**
 * A solution to the Regular Expression Matching problem.
 * URL: https://leetcode.com/problems/regular-expression-matching/submissions/
 */

function isMatch(s: string, p: string): boolean {
    return new RegExp(`^${p}$`).test(s);
};
