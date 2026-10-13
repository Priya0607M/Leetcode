class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_nums = min(nums)
        max_nums = max(nums)

        s = set(nums)
        ans = []

        for i in range(min_nums,max_nums+1):
            if i not in s:
                ans.append(i)

        return ans        

        