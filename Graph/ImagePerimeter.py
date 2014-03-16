import sys;

class ImageClick:
    ImgArray=None;
    ClickRow=None;
    ClickCol=None;
    def __init__(self,imgArray,clickRow,clickCol):
        self.ImgArray=imgArray;
        self.ClickRow=clickRow;
        self.ClickCol=clickCol;

def PrintArray(array):
    for row in array:
         print row;
def GetSurrending(array,row,column):
     surr=[];
     if row<len(array)-1:
         surr.append([row+1,column]);
     if row>0:
         surr.append([row-1,column]);
     if column<len(array[0])-1:
         surr.append([row,column+1]);
     if column>0:
         surr.append([row,column-1]);
     if row<len(array)-1 and column<len(array[0])-1:
         surr.append([row+1,column+1]);
     if row<len(array)-1 and column>0:
         surr.append([row+1,column-1]);
     if row>0 and column<len(array[0])-1:
         surr.append([row-1,column+1]);
     if row>0 and column>0:
         surr.append([row-1,column-1]);
     for i in range(len(surr)-1,-1,-1):
         r=surr[i][0];
         c=surr[i][1];
         if array[r][c]=='.':
             surr.remove(surr[i]);
     return surr;
def Contains(linkedNodes,s):
     for ln in linkedNodes:
         if ln[0]==s[0] and ln[1]==s[1]:
             return 1;
     return 0;
def GetAllLinkedNodes(array,row,column):
     row=row-1;
     column=column-1;
     linkedNodes=[];
     node=[row,column];
     linkedNodes.append(node);
     currentIndex=0;
     while currentIndex<len(linkedNodes):
         currentRow=linkedNodes[currentIndex][0];
         currentCol=linkedNodes[currentIndex][1];
         surrending=GetSurrending(array,currentRow,currentCol);
         #print str(currentRow)+'----'+str(currentCol);
         #print surrending
         for s in surrending:
             if Contains(linkedNodes,s)==0:
                 linkedNodes.append(s);
         currentIndex=currentIndex+1;
     return linkedNodes;
def GetBoards(node,array):
     sum=0;
     row=node[0];
     col=node[1];
     if (row>0 and array[row-1][col]=='.') or row==0:
         sum=sum+1;
     if (col>0 and array[row][col-1]=='.') or col==0:
         sum=sum+1;
     if (row<len(array)-1 and array[row+1][col]=='.') or row==len(array)-1:
         sum=sum+1;
     if (col<len(array[0])-1 and array[row][col+1]=='.') or col==len(array[0])-1:
         sum=sum+1;
     return sum;
def CalculateBoard(array,row,column):
     if array[row-1][column-1]=='.':
         return 0;
     else:
         allNodes=GetAllLinkedNodes(array,row,column);
         sum=0;
         for node in allNodes:
             boards=GetBoards(node,array);
             sum=sum+boards;
         return sum;

AllList=[];

line = str(sys.stdin.readline());
while line[0:7]!='0 0 0 0':
    input=line.split(' ');
    rowNumber=int(input[0]);
    colNumber=int(input[1]);
    row=int(input[2]);
    col=int(input[3]);
    imgArray=[];
    for i in range(rowNumber):
        rowin=str(sys.stdin.readline());
        rowin=rowin[0:colNumber];
        rowList=[];
        for c in rowin:
            rowList.append(c);
        imgArray.append(rowList);
    node=ImageClick(imgArray,row,col);
    AllList.append(node);
    line = str(sys.stdin.readline());
resutList=[];
for node in AllList:
    result=CalculateBoard(node.ImgArray,node.ClickRow,node.ClickCol);
    resutList.append(result);
for r in resutList:
    print r;
