import datetime
class Solution(object):
    
    def __init__(self):
        self.memory = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    
    def dayOfTheWeek(self, day, month, year):
        d = datetime.date(year, month, day)
        return self.memory[datetime.date.isoweekday(d)-1]

if __name__ == '__main__':
    s = Solution()
    d = s.dayOfTheWeek(3,1,1971)
    print(d)