class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] = freq[ch] + 1
            else:
                freq[ch] = 1    
        for ch in s:
            if freq[ch]<k:
                parts = s.split(ch)
                maximum = 0        
                for part in parts:
                    ans = self.longestSubstring(part,k)
                    maximum = max(maximum,ans)

                return maximum 
        return len(s)           

     