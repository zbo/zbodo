__author__ = 'zbo'
import Common

def BigAdd(number_A=[],number_B=[]):
    Sum=[];
#    print number_A
#    print number_B

    reversed_A= Common.reverse(number_A)
    reversed_B= Common.reverse(number_B)
    
#    print reversed_A
#    print reversed_B

    maxLen=max(len(reversed_A),len(reversed_B));
    extra=0;
    for i in range(maxLen):
        if i<len(reversed_A) and i<len(reversed_B):
            temp=reversed_A[i]+reversed_B[i];
        else:
            if i<len(reversed_A):
                temp=reversed_A[i];
            else:
                temp=reversed_B[i];
        if extra==1:
            temp=temp+1;
        if temp<=9:
            extra=0;
        else:
            temp=temp-10;
            extra=1;
        Sum.append(temp)
    return Common.reverse(Sum)
