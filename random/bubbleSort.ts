
function swap(arr: Array<any>, i: any, j: any) {
    const temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

function bubbleSort(arr: Array<any>) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < arr.length - 1; j++) {
            if (arr[j] > arr[j + 1]) swap(arr, j, j + 1);
        }
    }
    return arr;
}

console.log(bubbleSort([1, 5, 3, 8, 2, 1]));