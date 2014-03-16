import sys

def cal(number):
    sum=0.0;
    currentNumber=1;
    while sum < number:
        sum=sum+float(1/float(currentNumber+1));
        currentNumber=currentNumber+1;
    return currentNumber-1;

array=[];
result=[];
line = float(sys.stdin.readline());
array.append(line);
while line!=0.00:
    line = float(sys.stdin.readline());
    array.append(line);
for nu in array:
    re=cal(nu);
    result.append(re);
for i in range(len(result)-1):
    print str(result[i])+" card(s)"




