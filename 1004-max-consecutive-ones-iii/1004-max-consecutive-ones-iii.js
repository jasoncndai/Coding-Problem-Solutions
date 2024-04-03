/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestOnes = function(nums, k) {
    // checking input of k 1s from left to right with sliding window
    // update max value based on if all values in window are 1
    let left = 0;
    let right = 0;
    let max = 0;
    let zeroCount = 0;
    while (right < nums.length) {
        if (nums[right] === 0) {
            zeroCount++;
        }
        // need to move one of the flips over to the right
        // move left pointer up to next zero to flip
        while (zeroCount > k) {
            if (nums[left] === 0) {
                zeroCount--;
            }
            left++;
        }
        max = Math.max(max, right - left + 1);
        right++;
    }
    return max;
};