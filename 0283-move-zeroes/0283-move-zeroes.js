/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let nonZeroFoundAt = 0;
    for (let i = 0; i < nums.length; i++){
        if (nums[i] != 0){
            nums[nonZeroFoundAt++] = nums[i];
        }
    }
    for (let i = nonZeroFoundAt; i < nums.length; i++){
        nums[i] = 0;
    }
};