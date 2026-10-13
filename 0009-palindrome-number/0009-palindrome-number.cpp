class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0))
         {
            return false;
         }

        int R = 0;
        while (x > R) 
        {
            int d = x % 10;
            R = R * 10 + d;
            x /= 10;
        }

        return (x == R || x == R / 10);
    }
};