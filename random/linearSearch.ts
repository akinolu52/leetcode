/**
 * useful for un-sorted arrays
 */

function linearSearchIndexOf(arr: Array<string | number>, find: string | number): number {
    for(let index in (arr as any)){
        const curr = arr[index as any];
        
        if (curr === find) return (index as unknown as number);
    }
    return -1;
};

function linearSearchIncludes(arr: Array<string | number>, find: string | number): boolean {
    for(let index in (arr as any)){
        const curr = arr[index as any];
        
        if (curr === find) return true;
    }
    return false;
};

function linearSearchFind(arr: Array<string | number>, cb: Function): string | number | undefined {
    for(let index in (arr as any)){
        const curr = arr[index as any];

        console.log(find)
        
        if (curr === find) return find;
    }
    return undefined;
};


let arr = ['pizza', 'orange', 'yoghut'];
let find = 'yoghut'
let cb = (x: string) => x === 'yoghut';

console.log(linearSearchFind(arr, cb))
