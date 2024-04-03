/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    // Intuition: find largest subarrays of 1s, keep track of zero count, window moves between 0s
    // Keep track of left of window, middle is the 0 inbetween two groups of 1s to be deleted, right is advancing pointer
    var zeroCount = 0;
    var sum = 0;
    var max = 0;
    var left = 0;
    var middle = 0;
    for (var right = 0; right < nums.length; right++){
        if (nums[right] == 0){
            zeroCount++
            // Reach second 0, middle goes to new 0, left goes to old zero
            while (zeroCount >= 2){
                left = middle+1;
                // middle = right;
                zeroCount--;
            }
            middle = right
        }
        sum = right - left;
        max = Math.max(sum, max);
    }
    return max;
};