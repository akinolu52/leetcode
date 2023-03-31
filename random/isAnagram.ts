
function isAnagram(strA: string, strB: string): boolean {
    const rearrangeString = (str: string): string => {
        /**
         * convert to a array
         * sort the array
         * convert the array to a list and return the re-arranged string
         */
        return [...str].sort((a, b) => a.localeCompare(b)).join('')
    }

    // an anagram string must have the same length
    if (strA.length !== strB.length) {
        return false;
    }

    return rearrangeString(strA) === rearrangeString(strB);
}

console.log(isAnagram("anagram", "nagaram"))
