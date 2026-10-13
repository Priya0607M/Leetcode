class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for num in nums:
            result ^= num

        return result    

        # another approach
        # freq={}
        # for num in nums:
        #     if num in freq:
        #         freq[num]+=1
        #     else:
        #         freq[num]=1
        # for num in nums:
        #     if freq[num]==1:
        #         return num
        