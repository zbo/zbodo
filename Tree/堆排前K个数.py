def swap(list,posA,posB):
    temp=list[posA];
    list[posA]=list[posB];
    list[posB]=temp;

def initHeap(list,i):
    while i!=0:
        j=i/2;
        if list[j]>list[i]:
            swap(list,j,i);
        i=j;

def findMin(heap,x,y,z):
    if heap[x]>=heap[y] and heap[z]>=heap[y]:
        return y;
    elif heap[x]>=heap[z] and heap[y]>=heap[z]:
        return z;
    else:
        return x;

def getLeft(heap,i):
    if 2*(i+1)-1<=len(heap)-1:
        return 2*(i+1)-1
    else:
        return -1;

def getRight(heap,i):
    if 2*(i+1)<=len(heap)-1:
        return 2*(i+1);
    else:
        return -1;

def reTidyHeapPeek(heap,i):
    if getLeft(heap,i)==-1:
        return;
    elif getRight(heap,i)==-1:
        if getLeft(heap,i)<heap[i]:
            swap(heap,i,getLeft(heap,i));
            reTidyHeapPeek(heap,getLeft(heap,i));
    else:
        minNumberPos=findMin(heap,i,getLeft(heap,i),getRight(heap,i));
        if minNumberPos!=i:
            swap(heap,minNumberPos,i);
            reTidyHeapPeek(heap,minNumberPos);


def addToHeap(heap,node):
    if node<heap[0]:#that means smaller than peak
        return;
    else:
        heap[0]=node;
        reTidyHeapPeek(heap,0);

#begin of main
needNumber=8;
list=[4,2,3,10,9,8,1,20,21,11,90,5,7,88,77,27,87,13]
for i in range(1,needNumber):
    initHeap(list,i);

heap=list[0:needNumber];
for i in range(needNumber,len(list)):
    addToHeap(heap,list[i]);

print list;
print heap

