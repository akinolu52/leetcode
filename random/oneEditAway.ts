// One Away: There are three types of edits that can be performed on strings: 
// insert a character, remove a character, or replace a character. 
// Given two strings, write a function to check if they are one edit (or zero edits) away.

function oneEditAway(str1: string, str2: string): boolean {
    const len = str1.length > str2.length ? str1.length : str2.length

    let str1Arr = str1.split('');
    let str2Arr = str2.split('');

    let editCount = 0;
    for (let i = 0; i < len; i++) {
        const a = str1Arr[i];
        const b = str2Arr[i];

        if (a !== b) {
            ++editCount;
            if (str1.length === str2.length) continue;
            if (len === str1.length) str2Arr.splice(i, 0, ' ');
            if (len === str2.length) str1Arr.splice(i, 0, ' ');
        }
    }

    return editCount < 2;
}

console.log(oneEditAway('pale', 'pay'));
console.log(oneEditAway('pale', 'pales'));
