class Solution(object):
    def __init__(self):
        self.table = []
        self.n = 0
        self.result = []
    
    def convert(self):
        r = []
        for arr in self.table:
            line = ''.join(arr)
            r.append(line)
        return r
                
    def print_table(self):
        for line in self.table:
            print(line)

    def initTable(self,n):
        line = []
        for j in range(n):
            for i in range(n):
                line.append('.')
            self.table.append(line)
            line = []
        self.n = n

    def find_possibe_column(self,row):
        possible = []
        for i in range(self.n):
            if self.check_table(row,i):
                possible.append(i)
        return possible

    def check_table(self, row, column):
        for i in range(self.n):
            if self.table[row][i] =='Q':
                return False
            if self.table[i][column] == 'Q':
                return False
        r = row
        c = column
        while row>=0 and row <self.n and column>=0 and column<self.n:
            if self.table[row][column] == 'Q':
                return False
            row = row + 1
            column = column + 1
        row = r
        column = c
        while row>=0 and row <self.n and column>=0 and column<self.n:
            if self.table[row][column] == 'Q':
                return False
            row = row - 1
            column = column - 1
        row = r
        column = c
        while row>=0 and row <self.n and column>=0 and column<self.n:
            if self.table[row][column] == 'Q':
                return False
            row = row + 1
            column = column - 1
        row = r
        column = c
        while row>=0 and row <self.n and column>=0 and column<self.n:
            if self.table[row][column] == 'Q':
                return False
            row = row - 1
            column = column + 1
        return True

    def put(self,n,row):
        for column in self.find_possibe_column(row):
            self.table[row][column] = 'Q'
            if row == self.n-1:
                self.print_table()
                self.result.append(self.convert())
            else:
                self.put(n, row+1)
            self.table[row][column] = '.'
            

    def solveNQueens(self,n):
        self.initTable(n)
        self.put(n, 0)
        return self.result
        

if __name__ == '__main__':
    s = Solution()
    d = s.solveNQueens(4)
    print(d)