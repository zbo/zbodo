'''
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"'''

class Solution(object):
    source = ""
    all = []
    long = ""
    def single_palindrome(self, index):
        result = self.source[index]
        k=1
        while index-k >= 0 and index+k <= len(self.source)-1:
            if self.source[index-k] == self.source[index+k]:
                result = self.source[index-k] + result + self.source[index+k]
                k = k+1
            else:
                break
        self.all.append(result)
        if len(result)>len(self.long):
            self.long = result

    def double_palindrome(self, index):
        if index >= len(self.source)-1:
            return
        if self.source[index] != self.source[index + 1]:
            return
        result = self.source[index] + self.source[index+1]
        k = 1
        while index - k >= 0 and index + 1 + k <= len(self.source) - 1:
            if self.source[index - k] == self.source[index + 1 + k]:
                result = self.source[index - k] + result + self.source[index + 1 + k]
                k = k + 1
            else:
                break
        self.all.append(result)
        if len(result) > len(self.long):
            self.long = result

    def longestPalindrome(self, s):
        self.source = s
        for i in range(len(s)):
            self.single_palindrome(i)
            self.double_palindrome(i)
        #print self.all
        return self.long


if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("lqlvciwekzxapmjxyddlaoqhfhwphamsyfwjinkfvciucjhdgwodvmnpkibumexvlsxxumvrznuuyqfavmgwfnsvfbrvqhlvhpxaqehsiwxzlvvtxsnmlilbnmvnxyxitxwoahjricdjdncvartepfpdfndxqoozkfpdmlpvshzzffsspdjzlhmamqooooor")
