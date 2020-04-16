class Solution(object):
    def __init__(self):
        self.memory = []

    def missingNumber(self, nums):
        for i in range(len(nums)):
            self.memory.append(i)
        for n in nums:
            if n < len(nums):
                self.memory[n] = 0
        print(self.memory)


if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 0]
    s.missingNumber(nums)
