
function printArray<T>(arr: T[]): void {
    for (let i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
}


const myArray = [1, 2, 3, 4, 5];
printArray<number>(myArray);
// printArray([1, 2, 3, 5]);