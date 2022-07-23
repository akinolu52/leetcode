/**
 * @url - hhttps://leetcode.com/problems/valid-parentheses/
 * 
 * Given a string s containing just the characters 
 * '(', ')', '{', '}', '[' and ']', 
 * determine if the input string is valid.
 * 
 * @constraint 
 * 1. Open brackets must be closed by the same type of brackets.
 * 2. Open brackets must be closed in the correct order.
 * 
 * @param string: 
 * @returns a boolean 
 */

function isValid(s: string): boolean {
    s = s.trim().replace(/\s+/g, '');
    if (s.length % 2 !== 0) return false;
    if (!((s.charAt(0) !== '(') || (s.charAt(0) !== '{') || (s.charAt(0) !== '['))) return false;

    const maps: Record<string, string> = {
        ')': '(', 
        '}': '{', 
        ']' : '[',
    };

    const stack: string[] = [];

    for(let char of s){
        if(!char || char === ' ') continue;
        
        if (!maps[char]){
            stack.push(char);
            continue;
        }
        if(stack.pop() !== maps[char]) return false;
    }


    return stack.length === 0;
};