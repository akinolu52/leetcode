/**
 * @url - https://dev.to/theabbie/minimum-cost-of-buying-candies-with-discount-aom
 * 
 * Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, 
 * return the minimum cost of buying all the candies.
 * A shop is selling candies at a discount. 
 * For every two candies sold, the shop gives a third candy for free.
 * 
 * @constraint 1 <= cost.length <= 100
 * 
 * @param costs 
 * @returns the sum of the minimum cost
 * 
 * eg: input [5,5] returns 10
 */

function MinimumCostOfCandies(costs: number[]) {
    const length = costs.length;

    if (length < 1 || length > 100) return;
    if (length === 2) return costs[0] + costs[1];
    
    const sortedCost = costs.sort((a, b) => b - a);

    let result: number = 0;
    let evenCount = 0;

    for (let index = 0; index < sortedCost.length; index++) {
        const element = sortedCost[index];

        ++evenCount;
        if (evenCount === 2) {
            evenCount = 0;
            sortedCost.splice(index + 1, 1);
        }

        result += element;
    }

    return result;
}

console.log("MinimumCostOfCandies : ", MinimumCostOfCandies([5,5]));
console.log("MinimumCostOfCandies : ", MinimumCostOfCandies([1, 2, 3]));
console.log("MinimumCostOfCandies : ", MinimumCostOfCandies([6,5,7,9,2,2]));
