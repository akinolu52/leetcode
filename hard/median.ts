
function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const m = nums1.length;
    const n = nums2.length;

    if ((m > 1000) || (m < 0)) return 0;
    if ((n > 1000) || (n < 0)) return 0;
    if (((m + n) > 2000) || ((m + n) < 1)) return 0;

    const arr = [...nums1, ...nums2].sort((a, b) => a - b);
    const len = arr.length;
    const isLengthEven = len % 2 === 0;

    if (!isLengthEven) {
        if (len === 1) {
            return Number(arr[len - 1]);
        } else {
            let mid = Math.floor(len / 2);

            if (mid > len) {
                return Number(arr[mid - 1]);
            }

            return Number(arr[mid]);
        }
    } else {
        const mid = len / 2;
        return Number((arr[mid] + arr[mid - 1]) / 2);
    }
};

const nums1 = [1, 3]
const nums2 = [2]

console.log('result ', findMedianSortedArrays(nums1, nums2));