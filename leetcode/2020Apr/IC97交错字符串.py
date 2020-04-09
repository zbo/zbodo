'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

"bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
"babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
"babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
'''





class Solution(object):
    def __init__(self):
        self.match = False
        self.memory = {}

    def isInterleave(self, s1, s2, s3):
        return self.single_search(s1,s2,s3)

    def single_search(self, s1, s2, s3):
        key = "{0}-{1}-{2}".format(s1, s2, s3)
        if key in self.memory:
            return self.memory.get(key)
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1 == 0:
            return s2 == s3
        if len2 == 0:
            return s1 == s3
        if s3 == s1 + s2 or s3 == s2 + s1:
            self.match = True
            return True
        if len3 != len1 + len2:
            return False
        if self.match:
            return True
        fromS1 = False
        fromS2 = False


        if s1[0] == s3[0]:
            fromS1 = self.single_search(s1[1:], s2, s3[1:])
            self.memory["{0}-{1}-{2}".format(s1[1:], s2, s3[1:])] = fromS1
            if fromS1:
                self.match = True
        if s2[0] == s3[0]:
            fromS2 = self.single_search(s1, s2[1:], s3[1:])
            self.memory["{0}-{1}-{2}".format(s1, s2[1:], s3[1:])] = fromS2
            if fromS2:
                self.match = True
        return fromS1 or fromS2


if __name__ == "__main__":
    s1="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3="babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    s = Solution()
    print(s.isInterleave(s1,s2,s3))
