class Solution:
    def hammingWeight(self, n: int) -> int:
        countset = 0

        while n!=0:
            countset = countset+1
            n = n&(n-1)   

        return countset        
                