
function steps(n: number): void {
    for(let i = 0; i < n; i++){
        const count = i + 1;
        const display = `${'#'.repeat(count)}${' '.repeat(n - count)}`
        console.log(display)
    }
}

let n;

n = 10;

steps(n);
