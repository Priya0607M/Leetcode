class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        sum_n=(n*(n+1))//2
        sum1 = sum(nums)

        return sum_n-sum1
