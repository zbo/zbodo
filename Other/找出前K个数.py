#begin of recurtion method
def getNeedNumberFromList(list,needNumber):
    halfPos = len(list)/2;
    listBigger=[];
    listSmaller=[];
    for i in range(0,len(list)):
        if list[i]>list[halfPos]:
            listBigger.append(list[i]);
        else:
            listSmaller.append(list[i]);
    if len(listBigger)==needNumber:
        return listBigger;
    elif len(listBigger)+1==needNumber:
        listBigger.append(list[halfPos]);
        return listBigger;
    elif len(listBigger)>needNumber:
        return getNeedNumberFromList(listBigger,needNumber);
    elif len(listBigger)+1<needNumber:
        return listBigger+getNeedNumberFromList(listSmaller,needNumber-len(listBigger));


#begin of main
needNumber=8;
list=[4,2,3,10,9,8,1,20,21,11,90,5,7,88]
result=getNeedNumberFromList(list,needNumber);
print result;

