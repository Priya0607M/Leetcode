class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        L_count = 0
        R_count = 0
        for ch in s:
            if ch == 'L':
                L_count += 1
            elif ch == 'R':
                R_count += 1
            if L_count == R_count:
                answer += 1
                L_count = 0
                R_count = 0
        return answer            
