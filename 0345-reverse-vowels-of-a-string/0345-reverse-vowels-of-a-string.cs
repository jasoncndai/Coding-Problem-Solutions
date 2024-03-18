public class Solution {
    public string ReverseVowels(string s) {
        int i = 0;
        int j = s.Length - 1;
        StringBuilder result = new StringBuilder(s);
        while (i < j){
            if ("aeiou".Contains(Char.ToLower(s[i])) && "aeiou".Contains(Char.ToLower(s[j]))){
                char temp = result[i];
                result[i] = result[j];
                result[j] = temp;
                i++;
                j--;
            }
            if (!"aeiou".Contains(Char.ToLower(s[i]))){
                i++;
            }
            if (!"aeiou".Contains(Char.ToLower(s[j]))){
                j--;
            }
        }
        return result.ToString();
    }
}