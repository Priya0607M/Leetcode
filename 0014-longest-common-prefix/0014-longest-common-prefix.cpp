class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        
        sort(strs.begin(),strs.end());
        string ans="";

        string f = strs[0];
        string l = strs[n-1];

        int i = 0;
        while(i<f.size() && i<l.size())
        {
            if(f[i]==l[i])
            {
                ans += f[i];
            }
            else
            {
                break;
            }
            i++;
        }

        return ans;
    }
};