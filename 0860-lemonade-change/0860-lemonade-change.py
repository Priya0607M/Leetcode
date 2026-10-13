class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five = five + 1
            elif bill == 10:
                ten = ten + 1 
                if five>=1:
                    five = five - 1
                else:
                    return False    
            else:
                if five>=1 and ten>=1:
                    five = five - 1
                    ten = ten - 1
                elif five>=3:
                    five = five - 3
                else:
                    return False 
        return True             
                   