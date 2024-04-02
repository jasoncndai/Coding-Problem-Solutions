/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {
    // Similar to Max Avg Subarray, initialize window and then slide window over
    var sum = 0;
    var vowels = "aeiou";
    for (var j of s.substring(0,k)){
        if (vowels.includes(j)){
            sum++;
        }
    }
    var max = sum;
    for (var i = k; i < s.length; i++) {
        // If next character is vowel, add 1 to sum
        if (vowels.includes(s[i])){
            sum++;
        }
        // if previous character no long in window is vowel, subtract 1 from sum
        if (vowels.includes(s[i-k])){
            sum--;
        }
        // compare current substring vowels with max vowel substring
        max = Math.max(max, sum);
    }
    return max;
};