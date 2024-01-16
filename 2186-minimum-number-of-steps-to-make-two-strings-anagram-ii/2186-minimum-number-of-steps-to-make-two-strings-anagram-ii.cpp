class Solution {
public:
    int minSteps(string s, string t) {
        // Finding largest subset of characters shared between two strings, counting the    characters that are not
    
        vector<int> freq(26);

        // This is the difference in characters between the two strings, add to vector in string a, subtract in string b, and take the remaining element values in vector
        for (char ch : s){
            freq[ch - 'a'] += 1;
        }

        for (char ch : t){
            freq[ch - 'a'] -= 1;
        }

        // Make vector elements absolute for final count
        for (int i = 0; i < freq.size(); i++){
            if (freq[i] < 0){
                freq[i] *= -1;
            }
        }
        return accumulate(freq.begin(), freq.end(), 0);
    }
};