/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    var res = [];
    var left = 1;
    var right = 1;
    for (var i = 0; i < nums.length; i++) {
        res[i] = left;
        left *= nums[i];
    }
    for (var i = nums.length - 1; i >= 0; i--) {
        res[i] *= right;
        right *= nums[i];
    }
    return res;
};