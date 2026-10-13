class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n+1)//2
        left_half = nums[:mid]
        right_half = nums[mid:]

        ans = [0]*n
        i = len(left_half)-1
        for k in range(0,n,2):
            ans[k]=left_half[i]
            i = i-1
        j = len(right_half)-1    
        for k in range(1,n,2):
            ans[k]=right_half[j]
            j = j-1  

        nums[:]=ans      

        
