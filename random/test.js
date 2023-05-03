const countChange = (money, coins) => {
    const arr = Array(money + 1).fill(0);

    arr[0] = 1;

    for (let i = 0; i < money; i++) {
        for (let j = coins[i]; j <= money; j++) {
            arr[j] += arr[j - coins[i]];
        }
    }

    return arr[money]
};