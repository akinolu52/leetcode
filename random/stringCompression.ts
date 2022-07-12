// Implement a method to perform basic string compression using the counts of repeated characters. 
// For example, the string aabcccccaaa would become a2blc5a3, 
// If the "compressed" string would not become smaller than the original string, 
// your method should return the original string.You can assume the string has only uppercase and lowercase letters(a - z)

// push a 
// check what's in the string = same as current then increment count
// if not the same, delete string content and push current

function stringCompression(str: string): string {
    let newString = '';

    let s = str[0];
    let count = 1;

    for (let i = 1; i < str.length; i++) {
        const element = str[i];

        if (s === (element)) {
            ++count;
        } else {
            newString += `${s}${count}`;

            s = element;
            count = 1;
        }
    }

    return newString.length < str.length ? newString : str;
}

console.log(stringCompression('aabcccccaaa'));

