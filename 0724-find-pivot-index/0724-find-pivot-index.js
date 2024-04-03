/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    // calculate sum and subtract left prefix sum from it each iteration
    let sum = 0;
    let leftSum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
    }
    for (let i = 0; i < nums.length; i++) {
        if (leftSum === sum - leftSum - nums[i]) {
            return i;
        }
        leftSum += nums[i];
    }

    return -1;
};