


function stringPatternSearch(text, pattern): number {
    let counter = 0;

    for (let i = 0; i < text.length; i++) {
        for (let j = 0; j < pattern.length; j++) {
            const patternChar = pattern[j];
            console.log('patternChar => ', patternChar, i, j);

            if (patternChar !== text[i + j]) break;

            if (j === pattern.length - 1) counter++;

        }
    }

    return counter;
}

const text = 'lolol';
const pattern = 'lol';


console.log(stringPatternSearch(text, pattern));
console.log(stringPatternSearch('lollipop', pattern));
