public class Solution {
    public string GcdOfStrings(string str1, string str2) {
        string substr = str1.Length < str2.Length ? str1 : str2;
        while (substr.Length > 0) {
            if (str1.Length % substr.Length == 0 && str2.Length % substr.Length == 0) {
                bool isGcd = true;
                for (int i = 0; i < str1.Length; i += substr.Length) {
                    if (str1.Substring(i, substr.Length) != substr) {
                        isGcd = false;
                        break;
                    }
                }
                if (isGcd) {
                    for (int i = 0; i < str2.Length; i += substr.Length) {
                        if (str2.Substring(i, substr.Length) != substr) {
                            isGcd = false;
                            break;
                        }
                    }
                }
                if (isGcd) {
                    return substr;
                }
            }
            substr = substr.Substring(0, substr.Length - 1);
        }
        return "";
    }
}