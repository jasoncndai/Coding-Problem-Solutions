using System.Text.RegularExpressions;

public class Solution {
    public string ReverseWords(string s) {
        string result = System.String.Empty;
        string[] words = s.Split(' ');
        Array.Reverse( words );
        foreach (var word in words){
            result = result + word + ' ';
        }
        return Regex.Replace(result.Substring(0, result.Length - 1).Trim(), @"\s+", " ");
    }
}