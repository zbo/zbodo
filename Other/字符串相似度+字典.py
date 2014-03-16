str1='asdfghj'
str2='asdgfhjk'
str1Len=len(str1)
str2Len=len(str2)


memory=[[-1 for col in range(str2Len)] for row in range(str1Len)]

def findMin(x,y,z):
    if x>=y and z>=y:
        return y;
    elif x>=z and y>=z:
        return z;
    else:
        return x;

def getDiff(str1SatrtPos,str2StartPos):

    if memory[str1SatrtPos-1][str2StartPos-1]!=-1:
        return memory[str1SatrtPos-1][str2StartPos-1];
    else:
        if str1SatrtPos<str1Len and str2StartPos<str2Len:
            if cmp(str1[str1SatrtPos:str1SatrtPos+1],str2[str2StartPos:str2StartPos+1])==0:
                return getDiff(str1SatrtPos+1,str2StartPos+1)
            else:
                ifDeleteStr1=getDiff(str1SatrtPos+1,str2StartPos)+1;
                ifDeleteStr2=getDiff(str1SatrtPos,str2StartPos+1)+1;
                ifDeleteStrBoth=getDiff(str1SatrtPos+1,str2StartPos+1)+1;
                minValue=findMin(ifDeleteStr1,ifDeleteStr2,ifDeleteStrBoth)
                memory[str1SatrtPos-1][str2StartPos-1]=minValue
                return minValue

        else:
            if str1SatrtPos==str1Len and str2StartPos==str2Len:
                memory[str1SatrtPos-1][str2StartPos-1]=0
                return 0;
            elif str1SatrtPos==str1Len and str2StartPos!=str2Len:
                memory[str1SatrtPos-1][str2StartPos-1]=str2Len-str2StartPos
                return str2Len-str2StartPos;
            else:
                memory[str1SatrtPos-1][str2StartPos-1]=str1Len-str1SatrtPos
                return str1Len-str1SatrtPos;

diff=getDiff(0,0);
print diff
