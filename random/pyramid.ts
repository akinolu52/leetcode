function pyramid(n: number) {
    let res = ''
    for (let i = 0; i < n; i++) {
        const padding = ' '.repeat(n - i - 1);
        const hashing = '#'.repeat((i * 2 ) + 1)
        res += `${padding}${hashing}${padding}\n`;
    }

    console.log();
    console.log('\n' + res);
};

console.log(pyramid(3))
