/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    for (let i = 0; i < chars.length; i++) {
        let count = 1;
        while (chars[i] === chars[i + 1]) {
            count++;
            chars.splice(i + 1, 1);
        }
        if (count > 1) {
            chars.splice(i + 1, 0, ...count.toString().split(''));
            i += count.toString().length;
        }
    }
};