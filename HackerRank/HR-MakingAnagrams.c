#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'makeAnagram' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING a
 *  2. STRING b
 */

int makeAnagram(string a, string b) {
    // Finding largest subset of characters shared between two strings, counting the    characters that are not
    
    vector<int> freq(26);
    
    // This is the difference in characters between the two strings, add to vector in string a, subtract in string b, and take the remaining element values in vector
    for (char ch : a){
        freq[ch - 'a'] += 1;
    }
    
    for (char ch : b){
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

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string a;
    getline(cin, a);

    string b;
    getline(cin, b);

    int res = makeAnagram(a, b);

    fout << res << "\n";

    fout.close();

    return 0;
}
