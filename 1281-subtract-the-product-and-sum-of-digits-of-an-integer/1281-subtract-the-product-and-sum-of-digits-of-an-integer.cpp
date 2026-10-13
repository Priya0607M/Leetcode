class Solution {
public:
    int subtractProductAndSum(int n) {
        int r;
        int p = 1;
        int s = 0;
        while(n>0)
        {
            r = n%10;
            n = n/10;
            p = p*r;
            s = s+r;
        }
        return p - s;
        
    }
};