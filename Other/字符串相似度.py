str1='asdgfgyi'
str2='asdgfhjk'
str1Len=len(str1)
str2Len=len(str2)

def findMin(x,y,z):
    if x>=y and z>=y:
        return y;
    elif x>=z and y>=z:
        return z;
    else:
        return x;

def getDiff(str1SatrtPos,str2StartPos):
    if str1SatrtPos<str1Len and str2StartPos<str2Len:
        if cmp(str1[str1SatrtPos],str2[str2StartPos])==0:
            return getDiff(str1SatrtPos+1,str2StartPos+1)
        else:
            ifDeleteStr1=getDiff(str1SatrtPos+1,str2StartPos)+1;
            ifDeleteStr2=getDiff(str1SatrtPos,str2StartPos+1)+1;
            ifDeleteStrBoth=getDiff(str1SatrtPos+1,str2StartPos+1)+1;
            return findMin(ifDeleteStr1,ifDeleteStr2,ifDeleteStrBoth)

    else:
        if str1SatrtPos==str1Len and str2StartPos==str2Len:
            return 0;
        elif str1SatrtPos==str1Len and str2StartPos!=str2Len:
            return len(str2);
        else:
            return len(str1);


diff=getDiff(0,0);
print diff