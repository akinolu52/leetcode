

function anagram(strA: string, strB: string): boolean {
    strA = strA.replace(/[^a-zA-Z]/g, '').toLowerCase();
    strB = strB.replace(/[^a-zA-Z]/g, '').toLowerCase();

    if (strA.length !== strB.length) return false;

    // const longest = strA.length > strB.length ? 'a' : 'b'
    // const len = longest === 'a' ? strA.length : strB.length;
    console.log(strA, strB)

    let i = 0;
    while (i < strA.length) {
        const char = strB[i];

        if (!strA.includes(char)) return false

        i++;
    }

    // console.log(strA, strB)

    return true;
}

console.log(anagram('m9D!', 'md'))
