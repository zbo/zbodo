class node:
    value=None;
    with2=None;
    with3=None;
    with5=None;
    with7=None;
    def __init__(self,value,with2,with3,with5,with7):
        self.with2=with2;
        self.with3=with3;
        self.with5=with5;
        self.with7=with7;
        self.value=value;
#-------------------------------------------------------------------------------
def initial():
    #n1=node(1,1,1,1,1);
    n2=node(2,1,1,0,0);
    n3=node(3,1,0,0,0);
    n4=node(4,0,0,0,0);
    n5=node(5,0,0,0,0);
    n6=node(6,0,0,0,0);
    n7=node(7,0,0,0,0);
    #base.append(n1);
    base.append(n2);
    base.append(n3);
    base.append(n4);
    base.append(n5);
    base.append(n6);
    base.append(n7);
#-------------------------------------------------------------------------------
def printbase():
    for i in range(len(base)):
        print base[i].value;
#-------------------------------------------------------------------------------
def printbasedetail(base):
    for i in range(len(base)):
        out=str(base[i].value)+" :"+str(base[i].with2);
        out=out+","+str(base[i].with3);
        out=out+","+str(base[i].with5);
        out=out+","+str(base[i].with7);
        print out;
#-------------------------------------------------------------------------------
def findResonableBase():
    resonableBase=[];
    for i in range(len(base)):
        if base[i].with2!=0 and base[i].with7==0:
            resonableBase.append(base[i]);
        else:
            resonableBase.append(base[i]);
            break;
    return resonableBase;
#-------------------------------------------------------------------------------
def findTheMultipler(node):
    if node.with2==0:
        return 2;
    elif node.with3==0:
        return 3;
    elif node.with5==0:
        return 5;
    elif node.with7==0:
        return 7;
    else:
        return None;
#-------------------------------------------------------------------------------
def MarkWithValue(i):
    if base[i].with2==0:
        base[i].with2=1;
    elif base[i].with3==0:
        base[i].with3=1;
    elif base[i].with5==0:
        base[i].with5=1;
    elif base[i].with7==0:
        base[i].with7=1;
#-------------------------------------------------------------------------------
def findRightBase(resonableBase):
    minList=[];
    minIndexList=[];
    min=resonableBase[0].value*findTheMultipler(resonableBase[0]);
    index=0;
    minList.append(min);
    minIndexList.append(index);
    for i in range(1,len(resonableBase)):
        temp=resonableBase[i].value*findTheMultipler(resonableBase[i]);
        if temp<minList[0]:
            minList=[];
            minIndexList=[];
            minList.append(temp);
            minIndexList.append(i);
        elif temp==minList[0]:
            minList.append(temp);
            minIndexList.append(i);
    result.append(minList[0]);
    n=node(minList[0],0,0,0,0);
    base.append(n);
    for i in range(len(minIndexList)):
        MarkWithValue(minIndexList[i]);
    if base[index].with2==1 and base[index].with3==1 and base[index].with5==1 and base[index].with7==1:
        base.remove(base[index]);
    return resonableBase[index];


#-------------------------------------------------------------------------------

result=[1,2,3,4,5,6,7];
base=[];
initial();


while len(result)<5000:
    resonableBase=findResonableBase();
##    printbasedetail(resonableBase);
##    print '============'
    rightBase=findRightBase(resonableBase);
##    printbasedetail(base);
##    print '............'
##    print result;
##    print '************'

print result[1000];


















