class Solution(object):
    def __init__(self):
        self.result = []
    
    def find_near_high(self, i, T):
        if i == len(T) - 1:
            return 0
        if T[i] < T[i+1]:
            return 1
        elif T[i] >= T[i+1] and self.result[i+1]==0:
            return 0
        else:
            val = T[i]
            current_index  = i
            step = self.result[i+1]
            total_steps = step + 1
            while step > 0:
                if val < T[current_index+total_steps]:
                    return total_steps
                else:
                    step = self.result[current_index+total_steps]
                    total_steps = total_steps + step
                    
            return 0     
                
    def dailyTemperatures(self, T):
        for n in T:
            self.result.append(0)
        for i in range(len(T)-1,-1,-1):
            days = self.find_near_high(i, T)
            self.result[i] = days
        print(self.result)
        return self.result


if __name__ == '__main__':
    s = Solution()
    a= [73,74,75,71,69,72,76,73]
    #a= [55,38,53,81,61,93,97,32,43,78]
    s.dailyTemperatures(a)
