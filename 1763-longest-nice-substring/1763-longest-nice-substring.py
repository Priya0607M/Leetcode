class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        for i in range(len(s)):

            if s[i].islower():
                opposite = s[i].upper()
            else:
                opposite = s[i].lower()    

            if opposite not in s:
                left = s[:i]
                right = s[i+1:]

                left_ans = self.longestNiceSubstring(left)
                right_ans = self.longestNiceSubstring(right)

                if len(left_ans) >= len(right_ans):
                    return left_ans
                else:
                    return right_ans 
        return s