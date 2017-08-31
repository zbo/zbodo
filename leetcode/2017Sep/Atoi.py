class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        for c in str:
            if c not in ['0','1','2','3','4','5','6','7','8','9','-','+']:
                index = str.index(c)
                instance = Solution()
                return instance.myAtoi(str[0:index])
        if str=="" or str=="-" or str=="+":
            return 0
        if ('-' in str) and ('+' in str):
            return 0
        if str.count('+')>1 or str.count('-')>1:
            return 0
        if int(str)>2147483647:
            return 2147483647
        if int(str)<-2147483648:
            return -2147483648
        return int(str)

if __name__ == "__main__":
    s=Solution()
    print s.myAtoi("1")
