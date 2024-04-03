/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    // apply below function to both arrays
    return [findElementsOnlyInFirstArray(nums1, nums2), findElementsOnlyInFirstArray(nums2, nums1)];
};

var findElementsOnlyInFirstArray = function(nums1, nums2) {
    // add all elements of nums2 to set
    let set = new Set(nums2);
    let result = new Set();
    for (let i = 0; i < nums1.length; i++) {
        if (!set.has(nums1[i])) {
            result.add(nums1[i]);
        }
    }
    return Array.from(result);
}