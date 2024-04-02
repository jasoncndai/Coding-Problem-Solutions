/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) {
    // initialize variables and the sliding window
    let sum = 0;
    for (let i = 0; i < k; i++){
        sum += nums[i];
    }
    let max = sum;
    // Loop through, subtract prev in window and add next in window
    for (let i = k; i < nums.length; i++){
        sum += nums[i] - nums[i-k];
        max = Math.max(sum, max);
    }
    return max / k;
};