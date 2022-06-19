/**
 * write a function that returns the nth digit of an integer sequence
 * 
 * @constraint 1 <= n <= 231 - 1
 * 
 * @param n - number
 * @returns - nth digit of input
 * 
 * eg: input 3, output 3
 * eg: input 11, output 0
 */

function NthDigit(n: number) {
    if (n < 1 || n > 230) return;
    
    let numStr = '';
    for (let index = 1; index <= n; index++) {
        numStr += index.toString();
    }

    return numStr[n - 1];
}

console.log("NthDigit: ", NthDigit(11));
