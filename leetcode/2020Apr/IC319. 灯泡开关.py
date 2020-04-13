class Solution(object):
    def __init__(self):
        self.memory = []

    def bulbSwitch(self, n):
        for i in range(n):
            self.memory.append(-1)
        for i in range(1, n + 1):
            curr = i
            while curr <= n:
                self.memory[curr - 1] = self.memory[curr - 1] * (-1)
                curr = curr + i
            print self.memory
        sum = 0
        for n in self.memory:
            if n == 1:
                sum = sum + 1
        return sum


if __name__=="__main__":
    s = "aabbccasd"
    s = list(s)
    s.sort()
    print s

