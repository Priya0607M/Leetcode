class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        answer=0
        
        for i in range(len(flowerbed)):

            if i==0:
                left = 0
            else:
                left = flowerbed[i-1] 

            if (i == len(flowerbed) - 1):
                right = 0
            else:
                right = flowerbed[i+1] 

            if flowerbed[i]==0:
                if left == 0 and right == 0:
                    flowerbed[i] = 1
                    answer = answer + 1       

        if answer >= n:
            return True
        else:
            return False                     
