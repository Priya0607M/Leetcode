class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(left,right):
            if left==right:
                return nums[left]
            mid = (left+right)//2
            left_sum = solve(left,mid)
            right_sum = solve(mid+1,right)

            left_best = float('-inf')
            curr = 0
            for i in range(mid,left-1,-1):
                curr +=nums[i]
                left_best = max(left_best,curr)
            

            right_best = float('-inf')
            curr = 0
            for i in range(mid+1,right+1):
                curr += nums[i]
                right_best = max(right_best,curr)

            return max(left_sum,right_sum,left_best+right_best)

        return solve(0,len(nums)-1)            