##很长的log file记录了用户访问amazon.com的过程，两列分别为 userID 和
##pageName.
##log从上倒下按照点击发生的时间顺序。找出最popular的3连击。
##eg:
##zhang welcome
##Li Hello
##Wang welcome
##Li books
##Wang Hello
##zhang books
##Li shopping cart
##Li checkout
##zhang shopping cart
##Wang camera
##zhang checkout
##最popular的3 combo是books -> shopping cart -> checkout


list=[1,2,3,6,4,5,1,2,3,4,5,6,7,2,4,3,1,3,1,2,3,5,6,7,8,3,3,2,4,4,3]
threeNodeList=[]
dic={};

for i in range(0,len(list)-2):
    threeNodeList.append(list[i:i+3])
for node in threeNodeList:
    if dic.has_key(str(node))==False:
        dic[str(node)]=1;
    else:
        dic[str(node)]+=1;

maxHit=0;
for k,v in dic.items():
    if maxHit<v:
        maxItem=k
        maxHit=v

print maxHit,maxItem