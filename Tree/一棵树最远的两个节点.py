import time;
ISOTIMEFORMAT='%Y-%m-%d %X'
def bigger(x,y):
    if x>y:
        return x;
    else:
        return y;

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

def getFarthestLeaf(root):
    if root==None:
        return 0;
    if root.left==None:
        left=0;
    else:
        left=getFarthestLeaf(root.left)+1;
    if root.right==None:
        right=0;
    else:
        right=getFarthestLeaf(root.right)+1;
    return bigger(left,right);

def getMaxLength(root):
    if root==None:
        return 0;
    else:
        L=getFarthestLeaf(root.left);
        R=getFarthestLeaf(root.right);
        withRoot=L+R+2;
        withoutRoot=bigger(getMaxLength(root.left),getMaxLength(root.right));
        return bigger(withRoot,withoutRoot)


class node:pass;
list=[];
for i in range(0,10):
    n=node()
    n.data=i;
    n.left=None;
    n.right=None;
    list.append(n);
makeTree(list);
print getFarthestLeaf(list[0]);
print getMaxLength(list[0]);
print time.strftime( ISOTIMEFORMAT, time.localtime())

##print list[0].right.data
##print list[5].right is None






