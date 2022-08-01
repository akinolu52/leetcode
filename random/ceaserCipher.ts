
function ceaserCipher(str: string, shift: number): string {
    const alphabetArray = 'abcdefghijklmnopqrstuvwxyz';
    let newStr = '';

    str = str.toLowerCase();

    for (let i = 0; i < str.length; i++) {
        const char = str[i];
        const position = alphabetArray.indexOf(char);
        let newPosition = position + shift;

        if (position === -1) {
            newStr += char;
            continue;
        }

        if (newPosition > 25) {
            newPosition %= 26;
        }

        newStr += alphabetArray[newPosition];
    }

    return newStr;
}

let str, shift;

str = 'abcd'; // wxyz
shift = 100;

console.log(ceaserCipher(str, shift));
