// URLify: Write a method to replace all spaces in a string with '%20'. 
// You may assume that the string has sufficient space at the end to hold the additional characters, 
// and that you are given the "true" length of the string. 

// looping through each items
function URLify(str: string, len: number): string {
    let url = '';

    for (let i = 0; i < len; i++) {
        const element = str[i];

        if(element === ' '){
            url += '%20';
        } else {
            url += element;
        }
    }
    
    return url;
}

// using replace or replaceAll function
function URLify2(str: string, len: number): string {
    // return str.slice(0, len).replaceAll(' ', '%20'); // this should work on new JS/TS compiler
    return str.slice(0, len).replace(new RegExp(' ', 'g'), '%20');
}


console.log(URLify('Mr 3ohn Smith       ', 13))
console.log(URLify2('Mr 3ohn Smith     ', 13))