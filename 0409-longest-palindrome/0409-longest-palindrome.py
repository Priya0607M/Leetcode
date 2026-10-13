class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        answer = 0 
        has_odd = False       
        for value in count.values():
            if value%2==0:
                usable = value
            else:
                usable = value - 1 
                has_odd = True
            answer = answer + usable  
        if has_odd:
            answer = answer + 1  

        return answer                   