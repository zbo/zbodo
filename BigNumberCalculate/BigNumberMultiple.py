from BigNumberAdd import BigAdd
from Common import reverse

def MultipleSingle(listIn,num):
    result=[]
    reverse_listIn=reverse(listIn)
    temp_extra=0
    temp_mod=0
    for i in reverse_listIn:
        temp=i*num
        temp=temp+temp_mod;
        temp_extra=temp%10
        temp_mod=int(temp/10)
        result.append(temp_extra)
    if temp_mod!=0:
        result.append(temp_mod)
    return reverse(result)

def AddFollowingZero(temp, counter):
    while counter>0:
        counter=counter-1
        temp.append(0)
    return temp

def MultipleLists(listA,listB):
    listB=reverse(listB)
    tempAddList=[0]
    counter=0
    for i in listB:
        temp=MultipleSingle(listA,i)
        temp=AddFollowingZero(temp,counter)
        counter=counter+1
        tempAddList= BigAdd(tempAddList,temp)
    return tempAddList

