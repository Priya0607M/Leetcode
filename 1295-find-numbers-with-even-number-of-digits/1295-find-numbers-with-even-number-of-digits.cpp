class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int n = nums.size();
        int num;
        int count=0;
        for(int i=0;i<n;i++)
        {
            num = nums[i];
            int d=0;
            while(num>0)
            {
                num=num/10;
                d += 1;
            }
            if(d%2==0)
            {
                count = count + 1;
            }
        }
        return count;
        
    }
};