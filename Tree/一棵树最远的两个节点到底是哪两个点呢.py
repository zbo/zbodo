import copy
def makeTree(list):
    list[0].left=list[1];
    list[0].right=list[2];
    list[1].left=list[3];
    list[1].right=list[4];
    list[2].left=list[5];
    list[3].left=list[6];
    list[3].right=list[7];
    list[5].left=list[8];
    list[5].right=list[9];

leaves=[];
path_stack=[];
path=[];

def printDetail(list):
    message='[';
    for node in list:
       message=message+str(node.data)+',';
    message+=']';
    print message

def findAllLeaves(root):
    path_stack.append(root);
    if root.left==None and root.right==None:
        leaves.append(root);
        #printDetail(path_stack);
        #follow code is deepcopy in python
        path.append(copy.deepcopy(path_stack));
    if root.left!=None:
        findAllLeaves(root.left);
    if root.right!=None:
        findAllLeaves(root.right);
    path_stack.remove(root);

def reverse(list):#python 2.6 support list reverse
    temp=[]
    for i in range(len(list)-1,-1,-1):
        temp.append(list[i]);
    return temp;

def genPath(list1,list2):
    for i in range(len(list1)-1,-1,-1):
        for j in range(len(list2)-1,-1,-1):
            if list1[i].data==list2[j].data:
                listout=reverse(list1[i+1:]);
                listout.append(list[i]);
                listout+=list2[j+1:];
                return listout

def findLongPath(path):
    longestPath=0;
    for i in range(0,len(path)):
        for j in range(i+1,len(path)):
            realPath=genPath(path[i],path[j]);
            #printDetail(realPath);
            if len(realPath)>=longestPath:
                printDetail(realPath)
                longestPath=len(realPath)

class node:pass;
list=[];
for i in range(0,10):
    n=node()
    n.data=i;
    n.left=None;
    n.right=None;
    list.append(n);
makeTree(list);
findAllLeaves(list[0]);
leaves.append(list[0])

findLongPath(path);



