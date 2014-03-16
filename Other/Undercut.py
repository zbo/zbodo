import sys;
def GenResult(listA,listB):
    scoreA=0;
    scoreB=0;
    for i in range(len(listA)):
        #print str(listA[i])+'--'+str(listB[i]);
        valueA=int(listA[i]);
        valueB=int(listB[i]);
        if valueA==valueB:
            continue;
        elif valueA==1 and valueB==2:
            scoreA=scoreA+6;
        elif valueA==2 and valueB==1:
            scoreB=scoreB+6;
        elif valueA==valueB+1:
             scoreB=scoreB+valueA+valueB;
        elif valueA==valueB-1:
             scoreA=scoreA+valueA+valueB;
        elif valueA>valueB:
            scoreA=scoreA+valueA;
        else:
            scoreB=scoreB+valueB;
    result="A has "+str(scoreA)+" points. B has "+str(scoreB)+" points."
    return result;

line=sys.stdin.readline();
number=int(line);
printBuffer=[];
while number!=0:
    listAin=sys.stdin.readline();
    listBin=sys.stdin.readline();
    listA=[];
    listB=[];
    listAin=listAin.split(' ');
    listBin=listBin.split(' ');
    for i in range(len(listAin)):
        listA.append(int(listAin[i]))
        listB.append(int(listBin[i]))
    printBuffer.append(GenResult(listA,listB));
    line=sys.stdin.readline();
    number=int(line);
for i in range(len(printBuffer)):
    print printBuffer[i];
    if i<len(printBuffer)-1:
        print
