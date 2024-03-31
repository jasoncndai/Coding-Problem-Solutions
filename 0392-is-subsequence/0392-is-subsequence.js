/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let subs = 0;
    for (let cur = 0; cur < t.length; cur++){
        if (t[cur] == s[subs]){
            subs++;
        }
    }
    return subs == s.length;
};