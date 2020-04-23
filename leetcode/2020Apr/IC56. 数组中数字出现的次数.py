class Solution(object):
    def singleNumbers(self, nums):
        res = 0
        for i in nums:
            res = res^i

        idx = 1
        while idx & res == 0:
            idx = idx << 1
    
        a,b = 0,0
        for i in nums:
            if i & idx==0:
                a = a^i
            else:
                b = b^i
        return([a,b])

if __name__ == '__main__':
    s = Solution()
    nums =  [4,1,4,6]
    print(s.singleNumbers(nums))