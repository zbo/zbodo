'''
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

'''


class Solution(object):
    def __init__(self):
        self.INT_MAX = 2 ** 31 - 1
        self.INT_MIN = -2 ** 31
        self.minus = False
        self.minusSet = False

    def myAtoi(self, str):
        self.minus = False
        self.minusSet = False
        result = 0
        array = []
        for c in str:
            if c.strip() == "":
                if len(array) != 0:
                    break
                if self.minusSet:
                    break
                continue
            if c == "+":
                if self.minusSet or len(array) != 0:
                    break
                self.minusSet = True
                continue
            if c == "-":
                if self.minusSet or len(array) != 0:
                    break
                self.minusSet = True
                self.minus = True
                continue
            if c >= '0' and c <= '9':
                array.append(c)
            else:
                break
        length = len(array)
        for i in range(length):
            result = result + int(array[i]) * 10 ** (length - i - 1)
            if result >= self.INT_MAX and self.minus == False:
                return self.INT_MAX
            if result >= self.INT_MIN * (-1) and self.minus == True:
                return self.INT_MIN
        if self.minus:
            return result * (-1)
        else:
            return result


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("  42"))
    print(s.myAtoi("-42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("+1"))
    print(s.myAtoi("+-2"))
    print(s.myAtoi("   +0 123"))
    print(s.myAtoi("-2147483647"))
    print(s.myAtoi("-   234"))
    print(s.myAtoi("0-1"))
    print(s.myAtoi("-5-"))
