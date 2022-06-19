/**
 * @url - https://dev.to/theabbie/smallest-good-base-5djb
 * 
 * Given a string 'n' return the smallest good base of n
 * 
 * @constraint n is an integer in the range [3, 1018]
 * @constraint n does not contain any leading zeros
 * 
 * @param n - string number
 * @returns - smallest good base of n
 * 
 * eg: input '13' output '3'
 * eg: input '4681' output '8'
 */

function SmallestGoodBase(n: string) {
    let nNumber = Number(n);

    if (nNumber < 3 || nNumber > 1018) return;
    if (nNumber.toString() !== n) return;

    let maxVal = Math.max(...((n.split('').join(',').split(',').map(x => Number(x)))));

    let result = parseInt(n, 10).toString(maxVal);

    if (!result.includes('2')) {
        return maxVal;
    } else {
        return SmallestGoodBase(result);
    }
}

console.log('SmallestGoodBase: ', SmallestGoodBase('13'));
console.log('SmallestGoodBase: ', SmallestGoodBase('004681'));
console.log('SmallestGoodBase: ', SmallestGoodBase('1000000000000000000'));

