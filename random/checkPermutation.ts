// Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
// eg dog => god

// check if it's in the array string
function checkPermutation(str1: string, str2: string): boolean {
    if (str1.length !== str2.length) return false;

    const charArr1 = Array.from(str1);
    const charArr2 = Array.from(str2);

    for (let i = 0; i < charArr1.length; i++) {
        const element = charArr1[i];
        if (!charArr2.includes(element)) return false;
    }

    return true;
}


// using sort 
function checkPermutation2(str1: string, str2: string): boolean {
    if (str1.length !== str2.length) return false;

    const str1Sorted = [...str1].sort((a, b) => a.localeCompare(b));
    const str2Sorted = [...str2].sort((a, b) => a.localeCompare(b));

    return str1Sorted.every((val, index) => val === str2Sorted[index]);
}


console.log(checkPermutation('dog', 'ogd'))
console.log(checkPermutation2('dog', 'opd'));