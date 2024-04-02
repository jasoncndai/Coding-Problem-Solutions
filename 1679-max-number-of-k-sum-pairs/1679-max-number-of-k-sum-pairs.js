/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    // sort array, two pointers one at start and one at end
    // if sum is less than k, move start pointer to right
    // if sum is greater than k, move end pointer to left
    // if sum is equal to k, increment count and move both pointers
    nums.sort((a, b) => a - b);
    let start = 0;
    let end = nums.length - 1;
    let count = 0;
    while (start < end) {
        const sum = nums[start] + nums[end];
        if (sum === k) {
            count++;
            start++;
            end--;
        } else if (sum < k) {
            start++;
        } else {
            end--;
        }
    }
    return count;
};