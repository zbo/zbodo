'''Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        if x<-2147483648 or x>2147483647:
            return 0
        s=str(x)
        if s[0]=='-':
            ss=Solution()
            return -1*ss.reverse(int(s[1:]))
        else:
            t = list(s)
            l = len(t)
            for i,j in zip(range(l-1, 0, -1), range(l//2)):
                t[i], t[j] = t[j], t[i]
            result = int("".join(t))
            if result<-2147483648 or result>2147483647:
                return 0
            else:
                return result

if __name__ == "__main__":
    s=Solution()
    print s.reverse(123)
