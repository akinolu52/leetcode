// Is Unique: Implement an algorithm to determine if a string has all unique characters. 
function isUnique(str: string): boolean {
    const strSet = new Set([...str]);

    if (strSet.size !== str.length) return false;
    return true;
}

// What if you cannot use additional data structures?
function isUnique2(str: string): boolean {
    if (str.length > 128) return false;

    const charSet: boolean[] = new Array(128).fill(false);

    for (let i = 0; i < str.length; i++) {
        const element = str[i] as unknown as number;
        if (charSet[element]) return false;
        charSet[element] = true;
    }

    return true;
}

console.log(isUnique('abc-'))
console.log(isUnique2('a-+b-ucy'))