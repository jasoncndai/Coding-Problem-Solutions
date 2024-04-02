/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    // Using a map
    let map = {};
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        if (map[k - nums[i]] > 0) {
            count++;
            map[k - nums[i]]--;
        } else {
            map[nums[i]] = (map[nums[i]] || 0) + 1;
        }
    }
    return count;
};