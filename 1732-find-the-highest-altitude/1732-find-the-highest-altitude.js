/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    var prefix = 0;
    var max = 0;
    for (let i = 0; i < gain.length; i++){
        prefix += gain[i];
        max = Math.max(max, prefix);
    }
    return max;
};