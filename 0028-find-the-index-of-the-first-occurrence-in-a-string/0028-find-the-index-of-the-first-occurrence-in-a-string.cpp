class Solution {
public:
    int strStr(string haystack, string needle) {

        int n = haystack.size();
        int m = needle.size();

        int count=0;
        for(int i=0;i<n;i++)
        {
            if(haystack[i]==needle[0])
            {
                int a=0;
                int b=i;
                while(b<n && a<m && haystack[b]==needle[a])
                {
                    a++;
                    b++;
                }
                if(a==m)
                {
                    return i;
                }
            }
        }
        return -1;
    }
};