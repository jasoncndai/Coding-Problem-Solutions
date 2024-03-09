public class Solution {
    public string MergeAlternately(string word1, string word2) {
        string word3 = "";
        while (word1.Length > 0 && word2.Length > 0){
            word3 += word1[0];
            word3 += word2[0];
            word1 = word1.Substring(1);
            word2 = word2.Substring(1);
        }
        word3 += word1;
        word3 += word2;
        return word3;
    }
}