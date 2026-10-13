class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            result_arr=[]
            i=j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    result_arr.append(left[i])
                    i=i+1
                else:
                    result_arr.append(right[j])
                    j=j+1

            result_arr.extend(left[i:])
            result_arr.extend(right[j:])

            return result_arr

        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left_arr = self.sortArray(nums[:mid])
        right_arr = self.sortArray(nums[mid:])

        result = merge(left_arr,right_arr)

        return result                