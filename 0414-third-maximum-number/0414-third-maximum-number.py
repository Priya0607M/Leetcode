class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = set(nums)
        if len(nums)<3:
            return max(nums)
        else:
            temp=max(nums)
            nums.remove(temp)
            temp=max(nums)
            nums.remove(temp)

            return max(nums)
        