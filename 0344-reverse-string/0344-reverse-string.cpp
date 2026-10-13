class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size();
        char temp;
        int j = 0;
        int k = n-1;

        while(j<k)
        {
            temp = s[k];
            s[k] = s[j];
            s[j] = temp;

            j++;
            k--;
        }
    }
};