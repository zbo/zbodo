import sys;

def findNext(startIndex,currentBase,list):
    while startIndex<=len(list)-1:
        if(list[startIndex]>currentBase):
            return startIndex;
        else:
            startIndex=startIndex+1;
    return None;

def CalculateMaxSubsquence(list):
    startIndex=0;
    FirstNodeIndex=0;
    subSequence=[];
    subIndexList=[];
    currentBase=0;
    max=0;
    while FirstNodeIndex<len(list)-1:
        next=findNext(startIndex,currentBase,list);
        if next!=None:
            subSequence.append(list[next]);
            subIndexList.append(next);
            currentBase=list[next];
            startIndex=next+1;
        else:
            #print subSequence;
            if max<len(subSequence):
                max=len(subSequence);
            count=len(subSequence);
            removeIndex=subIndexList[count-1];
            subIndexList.remove(removeIndex);
            subSequence.remove(list[removeIndex]);
            if removeIndex==len(list)-1:#if meet the end of the list, remove 2
                removeIndex=subIndexList[count-2];
                subIndexList.remove(removeIndex);
                subSequence.remove(list[removeIndex]);
            if len(subSequence)!=0:#adjust the following node
                startIndex=removeIndex+1;
                currentBase=subSequence[len(subSequence)-1];
            else:#move the first node forward
                FirstNodeIndex=FirstNodeIndex+1;
                subIndexList.append(FirstNodeIndex);
                subSequence.append(list[FirstNodeIndex]);
                currentBase=list[FirstNodeIndex];
                startIndex=FirstNodeIndex+1;
    return max;

inputcount=str(sys.stdin.readline());
result=[];
for i in range(int(inputcount)):
    blank=str(sys.stdin.readline());
    numberCount=str(sys.stdin.readline());

    inputList = str(sys.stdin.readline());
    dataList=[];
    for data in inputList:
        if data!=' 'and data!='\n' and data!='\r':
            dataList.append(data);
    #dataList=[1, 7, 3, 5, 9, 4, 8];
    result.append(CalculateMaxSubsquence(dataList));

for s in result:
    print '\r';
    print s;
