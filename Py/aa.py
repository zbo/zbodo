def  StairCase(n):
    for i in range(1,n+1):
        str=' '*(n-i)+'#'*i
        print str


if __name__ == '__main__':
    StairCase(6)