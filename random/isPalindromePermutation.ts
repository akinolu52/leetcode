// Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome

function isPalindromePermutation(str: string): boolean {
    str = str.replace(new RegExp(' ', 'g'), '').toLowerCase()
    if (str === str.split('').reverse().join('')) return true;

    const charMap = new Map<string, number>();

    for (let i = 0; i < str.length; i++) {
        const element = str[i];
        const elementCount = str.length - str.replace(new RegExp(element, 'g'), '').length;
        charMap.set(element, elementCount)
    }

    let oddCount = 0;
    for (let [_, value] of charMap) {
        if (value % 2 !== 0) ++oddCount;
        if (oddCount > 1) return false;
    }

    return oddCount <= 1;
}

function isPalindromePermutation2(str: string): boolean {
    str = str.replace(new RegExp(' ', 'g'), '').toLowerCase()
    if (str === str.split('').reverse().join('')) return true;

    const charSet = new Set();

    for (let i = 0; i < str.length; i++) {
        const element = str[i];

        if (charSet.has(element)) charSet.delete(element);
        else charSet.add(element);
    }

    return charSet.size <= 1;
}


console.log(isPalindromePermutation('taco cat'));
console.log(isPalindromePermutation2('racecar'));

