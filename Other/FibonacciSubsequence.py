import sys;

def makeFibonacci(list,start,next):
    result=[list[start],list[next]];
    for i in range(next,len(list)):
        if list[i]==result[len(result)-1]+result[len(result)-2]:
            result.append(list[i]);
    return result;

def FindSub(list,start):
    for i in range(start+1, len(list)):
        next = i;
        result=makeFibonacci(list,start,next);
        if len(maxHolder)==0:
            maxHolder.append(result);
        else:
            if len(maxHolder[0])<len(result):
                maxHolder[0]=result;

def FindSubFibonacciLength(list):
    for i in range(0,len(list)):
        FindSub(list,i);

total=10;

maxHolder=[];
list=[];
while str(sys.stdin.readline())!='\n':
    data = str(sys.stdin.readline());
    temp=data.split(' ');
    for i in temp:
        list.append(int(i));
    FindSubFibonacciLength(list);
    print len(maxHolder[0]);
    string='';
    for i in maxHolder[0]:
        string=string+str(i)+' ';
    print string