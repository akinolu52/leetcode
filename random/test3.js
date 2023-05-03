
let input = `Beth,Charles,Danielle,Adam,Eric\n
17945, 10091, 10088, 3907, 10132\n
2, 12, 13, 48, 11`

const arr = input.split("\n")

let names = arr[0].split(',')
let values = arr[2].split(',')
let ages = arr[4].split(',')

const sortedNames = [...names].sort((a, b) => a.localeCompare(b))
console.log(sortedNames);

let nameResult = `${sortedNames}\n`;
let valueResult = "";
let ageResult = "";

for (let i = 0; i < sortedNames.length; i++) {
    const name = sortedNames[i];
    const index = names.findIndex((res) => res === name);

    valueResult += values[index] + ",";
    ageResult += ages[index] + ",";

    console.log('name ', name, index);

}
let k = nameResult + "\n" + valueResult + "\n" + ageResult;

console.log(k)

for (let index = 0; index < names.length; index++) {
    const name = names[index];
    const value = values[index];
    const age = ages[index];

    // console.log('name ', name, value, age);
}

console.log(names, values, ages)





// console.log(arr, names);

let nameDataObj = {}
let nameAgeObj = {}

// for (let index = 0; index < arr[0].length; index++) {
//     // const element = arr[index];

//     console.log(element)
//     // if (!element || index < 1) continue;

//     // nameDataObj[arr[0]]


//     // console.log('element ', element);

// }
