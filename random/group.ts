
function GroupSize(nums: number[]) {
    
    // const result: number[][] = [];
    const sortedNums = [...nums].sort();

    // const intermediate = {};

    // const uniqueNums = Array.from(new Set([...nums]));

    // for (let index = 0; index < uniqueNums.length; index++) {
    //     const element = uniqueNums[index].toString();

    //     const count = nums.toString().split(element).length - 1;

    //     intermediate[element] = count;
    //     // console.log('element: ', element, count);
    // }
    const initialValue = 0;

    const result = nums.reduce(
        (acc, cur, index) => {
            let res: any[] = [];
            // console.log(acc, cur);
            let key = cur;
            // console.log('key ', key);
            if (!acc[key]) {
                console.log('ok', key, index)
                // acc[key] = [index]
                res.push(index+ 0);
            }
            
            console.log('key ',  res);

            return acc;
        },
        initialValue
    );
    

    // for (let index = 0; index < nums.length; index++) {
    //     const element = nums[index];
    //     const elementCount = intermediate[element];
    //     result[element]= [index]

        
    //     // console.log('element: ', element, 'at', index, elementCount);
    // }
    

    // console.log(sortedNums, nums);
    
    // console.log(uniqueNums, intermediate);
    console.log(result);
    

}

console.log('GroupSize: ', GroupSize([3, 3, 3, 3, 3, 1, 3]));
