

function divideCorridor(corridor: string) {
    if (!/^[S,P]+$/.test(corridor)) return;

    const pLength = corridor.split('P').length - 1;
    const sLength = corridor.length - pLength;

    if (sLength % 2 !== 0 || sLength === 1) return '0p';
    if (sLength === 2) return 1;

    const result: any[] = []; // an array of partition index
    const indexArr: any[] = []
    let intermediate = '';

    let sCount = 0;

    for (let index = 0; index < corridor.length; index++) {
        const element = corridor[index];
        intermediate += element;

        // console.log( intermediate, index, sCount)

        if (element === 'S') ++sCount;
        if (sCount === 2) {
            indexArr.push(index);
            result.push(intermediate);
            const intermediateArr = [...intermediate];

            intermediateArr.splice(intermediateArr.indexOf('S'), 1)
            intermediate = intermediateArr.join('');
            sCount = 1;
       }
    }
    console.log('result: ', result);

    const result2: any[] = []; // an array of partition index
    intermediate = '';
    sCount = 0;

    let count = 0; 

    for (let index = corridor.length - 1; index > 0; index--) {
        const element = corridor[index];
        intermediate += element;

        // console.log( intermediate, index, sCount)

        if (element === 'S') ++sCount;
        if (sCount === 2) {
            indexArr.push(count);
            result2.push(intermediate);
            // const intermediateArr = [...intermediate];
            const intermediateArr = [...intermediate].reverse();

            intermediateArr.splice(intermediateArr.indexOf('S'), 1)
            intermediate = intermediateArr.reverse().join('');
            sCount = 1;
        }
        ++count;
        
    }


    console.log('result2: ', result2)

    console.log('index: ', indexArr);
    
    // console.log(sLength, pLength)

    
    return result.length;
}

// console.log('divideCorridor: ', divideCorridor('SSP'));
// console.log('divideCorridor: ', divideCorridor('SSPPSPS'));
// console.log('divideCorridor: ', divideCorridor('SS'));
// console.log('divideCorridor: ', divideCorridor('PPSPSP'));

console.log('divideCorridor: ', divideCorridor('PSPSPPSSPSSP'));

// > SSP
