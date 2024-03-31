/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    for (let cur = 0, lastNonZeroFoundAt = 0; cur < nums.length; cur++){
        if (nums[cur] != 0){
            let temp = nums[lastNonZeroFoundAt];
            nums[lastNonZeroFoundAt++] = nums[cur];
            nums[cur] = temp;
        }   
    }
        
};