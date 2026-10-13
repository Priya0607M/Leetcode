class Solution:
    def maximumTime(self, time: str) -> str:
        h1=time[0]
        h0=time[1]
        m1=time[3]
        m0=time[4]


        if h1 == '?' and h0 == '?':
            h1 = '2'
            h0 = '3'
        elif h1 == '?' and int(h0) <=3:
            h1 = '2'
        elif h1 == '?' and int(h0) <=9:
            h1 = '1'
        elif int(h1) <= 1 and h0 == '?':
            h0 = '9'
        elif int(h1) == 2 and h0 == '?':
            h0 = '3'  

        if m1 == '?' and m0 == '?':
            m1 = '5'
            m0 = '9'
        elif m1 == '?' and int(m0) <= 9:
            m1 = '5'
        elif int(m1) <= 5 and m0 == '?':
            m0 = '9'

        return h1 + h0 + ':' + m1 + m0       